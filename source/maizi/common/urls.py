#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
common模块的url配置。
"""

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ad$', views.ad, name='ad')
]
