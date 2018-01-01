# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as system_login, logout as system_logout
from forms import LoginForm,RegistForm
import json
from models import UserInfo


# @csrf_exempt
def login(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid(): # 判断所有参数是否符合要求
            user_name = request.POST.get('user_name', "")
            user_psw = request.POST.get('user_psw', "")
            user = authenticate(username=user_name, password=user_psw)
            # user = UserInfo.objects.filter(username=user_name, password=user_psw)
            if user:
                system_login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse("用户不存在或帐号密码错误")
        else:
            return render(request, "login.html", {
                "login_form": login_form,
                "errors": login_form.errors,
            })
    login_form = LoginForm()
    return render(request, "login.html", {
        "login_form": login_form,
    })

def regist(request):
    error = dict()
    if request.method == "POST":
        regist_form = RegistForm(request.POST)
        if regist_form.is_valid():
            user_name = request.POST.get('user_name', "")
            user_psw = request.POST.get('user_psw', "")
            some_one = UserInfo.objects.filter(username= user_name)
            if some_one:
                error['static'] = 0
                error['mgs'] = u"用户名已存在"
                return HttpResponse(json.dumps(error), content_type='application/json', status=200)
            users = UserInfo()
            users.username = user_name
            users.password = user_psw
            users.save()
            error['static'] = 1
            error['mgs'] = u"注册成功"
            return HttpResponse(json.dumps(error), content_type='application/json', status=200)

        error['static'] = 0
        error['mgs'] = u"请求方式不正确"
        return HttpResponse(json.dumps(error),content_type='application/json',status=200)
    regist_form = RegistForm()
    return render(request,"regist.html",{
        "regist_form":regist_form
    })

def logout(request):
    system_logout(request)
    return HttpResponseRedirect("/")

def forget_password(request):
    pass

def user_info(request):
    pass