# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Banner, Blog, Category, Tags


class BannerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Banner, BannerAdmin)


class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = (
            'kindeditor/kindeditor-all.js',
            'kindeditor/lang/zh_CN.js',
            'kindeditor/config.js',
        )



admin.site.register(Blog, BlogAdmin)


class TagsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tags, TagsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

