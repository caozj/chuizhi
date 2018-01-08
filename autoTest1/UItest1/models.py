from django.db import models

# Create your models here.

class Tester(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    yn = models.IntegerField()
    set_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name



class Object(models.Model):
    ob_name = models.CharField(max_length=100)
    ob_set_time = models.DateTimeField(auto_now=True)
    ob_mf_time = models.DateTimeField(auto_now=True)
    yn = models.IntegerField()
    tester = models.ForeignKey(Tester)
    ob_content = models.CharField(max_length=200)

    def __str__(self):
        return self.ob_name

class Block(models.Model):
    bk_name = models.CharField(max_length=100)
    bk_publick_YN = models.IntegerField()
    bk_set_time = models.DateTimeField(auto_now=True)
    bk_mf_time = models.DateTimeField(auto_now=True)
    yn = models.IntegerField()
    tester = models.ForeignKey(Tester)
    bk_content = models.CharField(max_length=200)
    boject = models.ForeignKey(Object)
    bk_sequence = models.IntegerField()

    def __str__(self):
        return self.bk_name

class Step(models.Model):
    sp_name = models.CharField(max_length=100)
    sp_set_time = models.DateTimeField(auto_now=True)
    sp_mf_time = models.DateTimeField(auto_now=True)
    yn = models.IntegerField()
    tester = models.ForeignKey(Tester)
    sp_content = models.CharField(max_length=200)
    block = models.ForeignKey(Block)
    sp_sequence = models.IntegerField()
    key_words = models.CharField(max_length=100,default='')   #关键字
    locate_way = models.CharField(max_length=100,default='')   #定位方式
    locate_content = models.CharField(max_length=120,blank=True,default='')   #定位内容
    value = models.CharField( max_length=120, default='', null=True, blank=True)    #值
    sp_assert = models.CharField(max_length=200,default='')  #断言

    def __str__(self):
        return self.sp_name

