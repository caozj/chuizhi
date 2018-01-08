from django.shortcuts import render
from django.contrib import auth  # 引入admin用户组
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required  # 装饰器，必须登录才能访问
from UItest1.models import Object, Block, Step, Tester  # 引入model类
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  # 引入分页器相关
from django.db import connection, transaction  # 数据库操作


# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['user'] = username
            response = HttpResponseRedirect('/auto_test/')
            return response
        else:
            return render(request, 'login.html', {'error': 'username or password is error'})
    else:
        return render(request, 'login.html')


@login_required
def auto_test(request):
    username = request.session.get('user', '')
    return render(request, 'auto_test.html', {'user': username})


@login_required
# 对应用户的项目列表
def object_list(request):
    username = request.session.get('user', '')
    object_list = Object.objects.filter(tester__name__exact=username).order_by("-id")
    pageinter = Paginator(object_list, 10)  # 每页两条数据
    page = request.GET.get('page', '')
    try:
        contacts = pageinter.page(page)  # 获得第几页的数据
    except PageNotAnInteger:
        # 如果page不是整数，获取第一页的数据
        contacts = pageinter.page(1)
    except EmptyPage:
        contacts = pageinter.page(pageinter.num_pages)
    return render(request, 'object_list.html', {'object_list': contacts})


# 编辑项目
def edit_object(request):
    field = request.POST.get('field', '')
    row_str = request.POST.get('row', '')
    row_dict = eval(row_str)
    try:
        cursor = connection.cursor()  # 建立游标
        new_value = row_dict[field]
        id = row_dict['id']
        update_sql = 'UPDATE UItest1_object SET %s ="%s" WHERE id=%s' % (field, new_value, id)
        cursor.execute(update_sql)
        return HttpResponse("ok")
        # transaction.commit_unless_managed() #提交数据库
    except:
        return HttpResponse("null_id")


# 增加项目
def add_object(request):
    username = request.session.get('user', '')
    tester = Tester.objects.get(name=username)
    Object.objects.create(ob_name='new_object', ob_set_time="", ob_mf_time='', yn=1, tester=tester,
                          ob_content='object_contant')
    return HttpResponse("ok")


# 删除项目
def delete_object(request):
    row_str = request.POST.get('row', '')
    row_dict = eval(row_str)
    try:
        id = row_dict['id']
        Object.objects.get(id=id).delete()
        return HttpResponse("ok")
    except:
        return HttpResponse("null")


# --------------------block-----------------------------


# 模块儿列表
def block_list(request, object_id):
    username = request.session.get('user', '')
    object = Object.objects.get(id=int(object_id))
    object_name = object.ob_name
    block_list = Block.objects.filter(tester__name__exact=username, boject_id=int(object_id)).order_by("bk_sequence","id")
    pageinter = Paginator(block_list, 10)  # 每页两条数据
    page = request.GET.get('page', '')
    try:
        contacts = pageinter.page(page)  # 获得第几页的数据
    except PageNotAnInteger:
        # 如果page不是整数，获取第一页的数据
        contacts = pageinter.page(1)
    except EmptyPage:
        contacts = pageinter.page(pageinter.num_pages)
    return render(request, 'block_list.html',
                  {'block_list': contacts, 'object_name': object_name, 'object_id': object_id})


# 新增模块儿
def add_block(request):
    username = request.session.get('user', '')
    tester = Tester.objects.get(name=username)
    object_id = request.POST.get('object_id', '')
    object = Object.objects.get(id=int(object_id))
    Block.objects.create(bk_name='new_block', bk_publick_YN=1, bk_set_time='', bk_mf_time='', yn=1, tester=tester,
                         bk_content='block_contant', boject=object, bk_sequence=99999)
    return HttpResponse("ok")


# 保存模块儿顺序
def save_block_sn(request):
    username = request.session.get('user', '')
    sn_json = request.POST.get('sn_json', '')
    sn_dict = eval(sn_json)
    for sn, id in sn_dict.items():
        Block.objects.filter(id=int(id)).update(bk_sequence=int(sn))
    return HttpResponse("ok")


# 编辑模块儿
def edit_block(request):
    field = request.POST.get('field', '')
    row_str = request.POST.get('row', '')
    row_dict = eval(row_str)
    try:
        cursor = connection.cursor()  # 建立游标
        new_value = row_dict[field]
        id = row_dict['id']
        update_sql = 'UPDATE UItest1_block SET %s ="%s" WHERE id=%s' % (field, new_value, id)
        cursor.execute(update_sql)
        return HttpResponse("ok")
        # transaction.commit_unless_managed() #提交数据库
    except:
        return HttpResponse("null_id")


# 删除模块儿
def delete_block(request):
    row_str = request.POST.get('row', '')
    row_dict = eval(row_str)
    try:
        id = row_dict['id']
        Block.objects.get(id=id).delete()
        return HttpResponse("ok")
    except:
        return HttpResponse("null")


# ----------------step----------------
def step_list(request, block_id):
    username = request.session.get('user', '')
    block = Block.objects.get(id=int(block_id))
    block_name = block.bk_name
    block_list = Step.objects.filter(tester__name__exact=username, block__id=int(block_id)).order_by("sp_sequence","id")
    pageinter = Paginator(block_list, 10)  # 每页两条数据
    page = request.GET.get('page', '')
    try:
        contacts = pageinter.page(page)  # 获得第几页的数据
    except PageNotAnInteger:
        # 如果page不是整数，获取第一页的数据
        contacts = pageinter.page(1)
    except EmptyPage:
        contacts = pageinter.page(pageinter.num_pages)
    return render(request, 'step_list.html',
                  {'step_list': contacts, 'block_name': block_name, 'block_id': block_id})


def add_step(request):
    username = request.session.get('user', '')
    tester = Tester.objects.get(name=username)
    block_id = request.POST.get('block_id', '')
    block = Block.objects.get(id=int(block_id))
    Step.objects.create(
        sp_name='new_step',
        sp_set_time='',
        sp_mf_time='',
        yn=1,
        tester=tester,
        block=block,
        sp_sequence=99999,
        key_words= 'XXX',
        locate_way='XXX',
        locate_content='XXX',
        value='XXX',
        sp_assert='XXX',
        sp_content='step_contant'
    )
    return HttpResponse("ok")


# 保存步骤顺序
def save_step_sn(request):
    username = request.session.get('user', '')
    sn_json = request.POST.get('sn_json', '')
    sn_dict = eval(sn_json)
    for sn, id in sn_dict.items():
        Step.objects.filter(id=int(id)).update(sp_sequence=int(sn))
    return HttpResponse("ok")


# 删除步骤
def delete_step(request):
    row_str = request.POST.get('row', '')
    row_dict = eval(row_str)
    try:
        id = row_dict['step_id']
        Step.objects.get(id=id).delete()
        return HttpResponse("ok")
    except:
        return HttpResponse("null")


# 编辑模块儿
def edit_step(request):
    field = request.POST.get('field', '')
    row_str = request.POST.get('row', '')
    row_dict = eval(row_str)
    try:
        cursor = connection.cursor()  # 建立游标
        new_value = row_dict[field]
        step_id = row_dict['step_id']
        update_sql = 'UPDATE UItest1_step SET %s ="%s" WHERE id=%s' % (field, new_value, step_id)
        cursor.execute(update_sql)
        return HttpResponse("ok")
        # transaction.commit_unless_managed() #提交数据库h
    except:
        return HttpResponse("null_id")

def test(request):
    return render(request, 'testx_table.html')
