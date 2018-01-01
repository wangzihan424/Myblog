# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings
from models import Banner, Blog, Category
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def loading_global_setting(request):
    diary_count = Blog.objects.all().count()
    run_time = datetime.now() - datetime(2016, 1, 1, 0, 0, 0, 0)
    run_time = run_time.days
    navs = Category.objects.all()
    return {
        "blog_title": settings.BLOG_TITLE,
        "blog_desc": settings.BLOG_DESC,
        "blog_diary_count": diary_count,
        "blog_run_time": run_time,
        "navs": navs,
        "upload_path": settings.MEDIA_URL,
    }


def index(request):

    banners = Banner.objects.order_by("img_position").all()

    return render(request, "index.html", {
        "banners": banners,
    })


def list(request, cate_id=0):
    cate_query_set = Category.objects.filter(id=cate_id)
    if cate_query_set:
        blog_query_set = Blog.objects.filter(cate_id_id=cate_id)
        paginator = Paginator(blog_query_set, 5)
        page = request.GET.get('page')
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        return render(request, "list.html", {
            "category": cate_query_set[0],
            "blogs": contacts,
        })
    else:
        return render(request, '404.html')


def show(request):
    return render(request, "show.html", {

    })
