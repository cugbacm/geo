from django.conf.urls import patterns, url
from geo import views

urlpatterns = patterns('', 
	url(r'^teacherList/$', views.teacherList, name = 'teacherList'),
	url(r'^index/$', views.index, name = 'index'),
	url(r'^zywcr/$', views.zywcr, name = 'zywcr'),
	url(r'^chengguojianjie/$', views.chengguojianjie, name = 'chengguojianjie'),
	url(r'^(?P<teacher_id>\d+)/teacher/$', views.teacher, name='teacher'),
)