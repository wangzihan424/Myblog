# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Banner(models.Model):
    img_src = models.ImageField(max_length=255, upload_to="banner/%Y/%m/", default="banner/default.png", verbose_name=u"图片来源")
    img_alt = models.CharField(max_length=100, verbose_name=u"图片名称")
    # positon表示图片编号,越小越靠前
    # 99 表示最后面
    img_position = models.SmallIntegerField(default=99, verbose_name=u"图片顺序")

    class Meta:
        verbose_name = u"广告轮播"
        verbose_name_plural = verbose_name

    # python2
    def __unicode__(self):
        return self.img_alt

    # python3
    # def __str__(self):
    #    return self.img_alt


# 用户表 - 成绩(user_id)
# 分类表 - 博客表(cate_id)

class Category(models.Model):
    cate_name = models.CharField(max_length=100, verbose_name=u"分类名称")

    class Meta:
        verbose_name = u"分类表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.cate_name


class Tags(models.Model):
    tag_name = models.CharField(max_length=100, verbose_name=u"标签")

    class Meta:
        verbose_name = u"标签表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tag_name

class Blog(models.Model):
    img_src = models.ImageField( max_length=255, upload_to="blog/%Y/%m/", default="blog/default.png", verbose_name=u"图片来源")
    img_alt = models.CharField(verbose_name=u"图片名称", max_length=100)
    blog_title = models.CharField(verbose_name=u"博客标题", max_length=100)
    blog_create_time = models.DateTimeField(verbose_name=u"发布时间", default=timezone.now)
    blog_edit_time = models.DateTimeField(verbose_name=u"修改时间", default=timezone.now)
    blog_look_num = models.IntegerField(verbose_name=u"浏览量", default=0)
    blog_comment_num = models.IntegerField(verbose_name=u"评论量", default=0)
    blog_content = models.TextField(verbose_name=u"博客内容", )
    # 分类   一篇博客 -- 一个分类     一个分类 -- 多个博客
    # 一对多的关系,使用外键
    cate_id = models.ForeignKey(Category, verbose_name=u"分类ID")
    # 标签   一篇博客 -- 多个标签     一个标签 -- 多个博客
    # 多对多 ManyToMany
    tags = models.ManyToManyField(Tags, verbose_name=u"标签")
    # 一对一  oneToOne
    # 一个学生对应一个身份证
    # 一对多  ForeignKey
    # 一个班级对应多个学生  一个学生对应一个班级
    # 多对多  ManyToMany
    # 一个学生对应多个老师  一个老师对应多个学生


    class Meta:
        verbose_name = u"博客表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.blog_title



# 一个张三 有数学,语文,外语三门成绩
# user    1  张三
# score   1  语文  90  1
        # 2 数学  95  1
        # 3 外语 100 1