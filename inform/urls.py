from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.urls import path

app_name = "inform"

urlpatterns = [
    path('inform', views.InformViewSet.as_view({'post': 'create', 'get': 'list'}), name='inform_list_create'),
    path('inform/<int:pk>', views.InformViewSet.as_view({'get': 'retrieve', 'delete': 'destroy'}), name='inform_detail_delete'),
    path('inform/read', views.ReadInformView.as_view(), name='read_inform'),
]