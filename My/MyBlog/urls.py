"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main import views as main_views
from django.views.static import serve
from django.conf import settings
from main.upload import upload_image
from Users import views as users_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', main_views.index),
    url(r'^cate/$', main_views.list, name="category"),
    url(r'^cate/(\d*)', main_views.list, name="category"),
    url(r'^show/', main_views.show),
    url(r'^uploads/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT,}),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^$', main_views.index),

    url(r'^login/', users_views.login, name='login'),
    url(r'^logout/', users_views.logout, name='logout'),
    url(r'^regist/', users_views.regist, name='regist'),

    url(r'^captcha/', include('captcha.urls')),
]
