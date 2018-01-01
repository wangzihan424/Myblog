# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


# 凡是继承自models.Model的模型将来都是新表
# class UserInfo(models.Model):

# 如果模型继承自AbstractUser,表示对系统的用户表做一个修改
class UserInfo(AbstractUser):
    user_phone = models.CharField(max_length=11, verbose_name=u"手机号")
    user_head = models.ImageField(upload_to="user/%Y/%m", default="user/default.png",max_length=255)

    class Meta:
        verbose_name = u"用户表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username