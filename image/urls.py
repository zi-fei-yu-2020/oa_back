# -*- coding: utf-8 -*-
# @Time    : 2024-07-03 1:22
# @Author  : 子非鱼
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views


urlpatterns = [
    path('upload', views.UploadImageView.as_view(), name='upload')
]