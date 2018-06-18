#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
@author: liudaoqiang
@file: studycase
@time: 2018/6/16 22:15
'''
from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^indextt/$', views.indextt),
	url(r'^indext/$', views.indext),
	url(r'^index/$', views.index),
	url(r'^article/(?P<article_id>[0-9]+)$', views.article_page,name='article_page'),
	url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page,name='edit_page'),
	url(r'^edit/action/$', views.edit_action,name='edit_action'),
]