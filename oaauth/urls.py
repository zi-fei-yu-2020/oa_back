# -*- coding: utf-8 -*-
# @Time    : 2024-06-19 23:03
# @Author  : 子非鱼
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views

app_name = 'oa_auth'

urlpatterns = [
    path('login', views.login),
    path('resetpwd', views.reset_pwd),
]
