from django.contrib import admin
from UItest1.models import Tester,Object,Block,Step
# Register your models here.

class TesterAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','email','yn']

class ObjectAdmin(admin.ModelAdmin):
    list_display = ['ob_name','ob_mf_time','yn','tester','ob_content']

class BlockAdmin(admin.ModelAdmin):
    list_display = ['bk_name','bk_publick_YN','bk_mf_time','yn','tester','bk_content','boject','bk_sequence']

class SetpAdmin(admin.ModelAdmin):
    list_display = ['sp_name','sp_mf_time','yn','tester','sp_content','block','sp_sequence']

admin.site.register(Tester,TesterAdmin)
admin.site.register(Object,ObjectAdmin)
admin.site.register(Block,BlockAdmin)
admin.site.register(Step,SetpAdmin)