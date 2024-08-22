# -*- coding: utf-8 -*-
# @Time    : 2024-07-02 16:20
# @Author  : 子非鱼
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'staff'

# router = DefaultRouter(trailing_slash=False)
# router.register("staff", views.StaffViewSet, basename='staff')

urlpatterns = [
                  path('departments', views.DepartmentListView.as_view(), name='departments'),
                  # # path('staff', views.StaffView.as_view(), name='staff_view'),
                  # path('active', views.ActiveStaffView.as_view(), name='active_staff'),
                  # path('download', views.StaffDownloadView.as_view(), name='download_staff'),
                  # path('upload', views.StaffUploadView.as_view(), name='upload_staff'),
                  # path('test/celery', views.TestCeleryView.as_view(), name='test_celery')
              ]
