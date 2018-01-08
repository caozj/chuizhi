"""autoTest1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from UItest1 import views
from UItest1.seleniumBase import selenium_view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',views.login),
    url(r'^auto_test/$',views.auto_test),
    url(r'^object_list/$',views.object_list),
    url(r'^test/$',views.test),
    url(r'^edit_object/$',views.edit_object),
    url(r'^add_object/$',views.add_object),
    url(r'^delete_object/$',views.delete_object),
    #----------------block------------------
    url(r'^block_list/(?P<object_id>[0-9]*)/$',views.block_list),
    url(r'^add_block/$',views.add_block),
    url(r'^save_block_sn/$',views.save_block_sn),
    url(r'^edit_block/$',views.edit_block),
    url(r'^delete_block/$',views.delete_block),
    #-------------------step-------------
    url(r'^step_list/(?P<block_id>[0-9]*)/$',views.step_list),
    url(r'^add_step/$',views.add_step),
    url(r'^save_step_sn/$',views.save_step_sn),
    url(r'^delete_step/$', views.delete_step),
    url(r'^edit_step/$', views.edit_step),
    url(r'^start_steps/(?P<block_id>[0-9]*)/$', selenium_view.start_steps),
    url(r'^start_blocks/(?P<object_id>[0-9]*)/$', selenium_view.start_blocks),


]
