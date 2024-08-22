from datetime import datetime

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from .serializers import LoginSerializer, UserSerializer, ResetPwdSerializer
from .authentications import generate_jwt
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def login(request):
    # 1. 验证数据是否可用
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data.get('user')
        user.last_login = datetime.now()
        user.save()
        token = generate_jwt(user)
        return Response({'token': token, 'user': UserSerializer(user).data})
    else:
        # person = ｛"username": "张三", "age": 18｝
        # person.values() = ['张三', 18] dict_values
        detail = list(serializer.errors.values())[0][0]
        # drf在返回响应是非200的时候，他的错误参数名叫detail，所以我们这里也叫做detail
        return Response({"detail": detail}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reset_pwd(request):
    from rest_framework.request import Request
    # request：是DRF封装的，rest_framework.request.Request
    # 这个对象是针对django的HttpRequest对象进行了封装
    serializer = ResetPwdSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        pwd1 = serializer.validated_data.get('pwd1')
        request.user.set_password(pwd1)
        request.user.save()
        return Response({"code": 200, "message": "密码修改成功"})
    else:
        print(serializer.errors)
        detail = list(serializer.errors.values())[0][0]
        return Response({"detail": detail}, status=status.HTTP_400_BAD_REQUEST)
