from django.shortcuts import render
from django.contrib import auth  # 引入admin用户组
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required  # 装饰器，必须登录才能访问
from UItest1.models import Object, Block, Step, Tester  # 引入model类
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage  # 引入分页器相关
from django.db import connection, transaction  # 数据库操作
from UItest1.seleniumBase import operation


def start_steps(request,block_id,op_base = operation.operationBase()):
    username = request.session.get('user', '')
    tester = Tester.objects.get(name=username)
    block = Block.objects.get(id=int(block_id))
    step_list = Step.objects.filter(tester=tester,block=block,yn=1).order_by("sp_sequence","id")
    op_base = op_base
    for step in step_list:
        if step.key_words =='open_browser':
            op_base.openChrome()
        elif step.key_words =='set_ulr':
            op_base.setURL(step.value)
        elif step.key_words =='click':
            element = op_base.operationBase_find_element(step.locate_way, step.locate_content)
            element.click()
        elif step.key_words =='input':
            element = op_base.operationBase_find_element(step.locate_way,step.locate_content)
            op_base.input(element,step.value)
        elif step.key_words =='close':
            op_base.close()
    return HttpResponse("ok")

def start_blocks(request,object_id):
    username = request.session.get('user', '')
    tester = Tester.objects.get(name=username)
    object = Object.objects.get(id=int(object_id))
    block_list = Block.objects.filter(tester=tester, boject=object, yn=1).order_by("bk_sequence","id")
    op_base = operation.operationBase()
    for block in block_list:
        start_steps(request,block.id,op_base)
    return HttpResponse("ok")

# ID = "id"
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"
