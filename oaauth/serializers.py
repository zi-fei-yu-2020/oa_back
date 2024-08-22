# -*- coding: utf-8 -*-
# @Time    : 2024-06-19 22:52
# @Author  : 子非鱼
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers, exceptions

from oaauth.models import OAUser, UserStatusChoices, OADepartment


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=20, min_length=6)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = OAUser.objects.filter(email=email).first()
            if not user:
                raise serializers.ValidationError("请输入正确的邮箱！")
            if not user.check_password(password):
                raise serializers.ValidationError("请输入正确的密码！")
            # 判断状态
            if user.status == UserStatusChoices.UNACTIVE:
                raise serializers.ValidationError("该用户尚未激活！")
            elif user.status == UserStatusChoices.LOCKED:
                raise serializers.ValidationError("该用户已被锁定，请联系管理员！")
            # 为了节省执行SQL语句的次数，这里我们把user直接放到attrs中，方便在视图中使用
            attrs['user'] = user
        else:
            raise serializers.ValidationError('请传入邮箱和密码！')
        return attrs


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = OADepartment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = OAUser
        # fields = "__all__"
        exclude = ('password', 'groups', 'user_permissions')


class ResetPwdSerializer(serializers.Serializer):
    oldpwd = serializers.CharField(min_length=6, max_length=20)
    pwd1 = serializers.CharField(min_length=6, max_length=20)
    pwd2 = serializers.CharField(min_length=6, max_length=20)

    def validate(self, attrs):
        oldpwd = attrs['oldpwd']
        pwd1 = attrs['pwd1']
        pwd2 = attrs['pwd2']

        user = self.context['request'].user
        if not user.check_password(oldpwd):
            raise exceptions.ValidationError("旧密码错误！")

        if pwd1 != pwd2:
            raise exceptions.ValidationError("两个新密码不一致！")
        return attrs
