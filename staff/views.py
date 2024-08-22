from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from oaauth.models import OADepartment, UserStatusChoices
from oaauth.serializers import DepartmentSerializer


class DepartmentListView(ListAPIView):
    queryset = OADepartment.objects.all()
    serializer_class = DepartmentSerializer
