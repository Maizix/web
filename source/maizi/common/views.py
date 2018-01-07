#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
Common模块View业务处理。
"""

import logging
from django.shortcuts import render, HttpResponse
from .models import *
from django.core.serializers import serialize
import json
from itertools import chain
from django.conf import settings
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger


logger = logging.getLogger('common.views')


def global_setting(request):
    media_url = settings.MEDIA_URL
    # 广告
    ad_list = Ad.objects.all()[:3]
    # 搜索推荐
    rkw_list = RecommendKeywords.objects.all()[:8]

    return locals()


# 首页
def index(request):
    # 课程
    clist = Course.objects.all()
    # 课程-最新
    course_new_list = getpage(request, clist.order_by('-date_publish')[:40])
    # 课程-最多播放
    course_most_list = getpage(request, clist.order_by('-click_count')[:40])
    # 课程-最多人气
    course_hot_list = getpage(request, clist.order_by('-student_count')[:40])
    return render(request, "common/index.html", locals())


# 分页
def getpage(request, list):
    paginator = Paginator(list, 8)
    try:
        page = int(request.GET.get('page', 1))
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list


# 广告
def ad(request):
    try:
        cid = request.GET.get('cid',None)
    except Exception as e:
        logger.error(e)
    # 可根据cid找到对应课程.此处省略.
    return render(request, 'class.html', {'cid': cid})


# 搜索
def search(request):
    try:
        word = request.GET.get('word','')
        clist = ''
        if word:
            cc_list = CareerCourse.objects.filter(name__contains=word)[:10]
            c_list = Course.objects.filter(name__contains=word)[:10]
            clist = chain(cc_list, c_list)
            clist = json.dumps(serialize('json', clist))
    except Exception as e:
        logger.error(e)
    return HttpResponse(clist, content_type='application/json')



