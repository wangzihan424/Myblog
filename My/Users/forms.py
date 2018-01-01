# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from django import forms
from captcha.fields import CaptchaField
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    # 用户名最少5位,最多10位
    user_name = forms.CharField(
        min_length=5,
        label=_(u"用户名"),
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    # 密码至少六位,最多20位,需要限制密码强度  widget:小部件
    user_psw = forms.CharField(
        min_length=6,
        max_length=20,
        label=_(u"密码"),
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    captcha = CaptchaField(
        label=_(u"验证码")
    )
    login = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "type": "submit",
                "class": "btn btn-default",
                "value": _(u"登录")
            }
        )
    )

class RegistForm(forms.Form):
    # 用户名最少5位,最多10位
    user_name = forms.CharField(
        min_length=5,
        label=_(u"用户名"),
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    # 密码至少六位,最多20位,需要限制密码强度  widget:小部件
    user_psw = forms.CharField(
        min_length=6,
        max_length=20,
        label=_(u"密码"),
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    regist = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "type": "submit",
                "class": "btn btn-default",
                "value": _(u"注册")
            }
        )
    )


