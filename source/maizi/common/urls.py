#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
common模块的url配置。
"""

from django.conf.urls import url
from . import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # 显示上传的图片,配合setting中的media root&url使用
    url(r'^upload/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT, }),
    url(r'^ad$', views.ad, name='ad'),
    url(r'^search$', views.search, name='search'),
]
