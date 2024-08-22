# -*- coding: utf-8 -*-
# @Time    : 2024-06-17 2:33
# @Author  : 子非鱼
# @File    : init_user.py
# @Software: PyCharm
from django.core.management.base import BaseCommand
from oaauth.models import OAUser, OADepartment


class Command(BaseCommand):
    def handle(self, *args, **options):
        departments = {
            'admin': OADepartment.objects.get(name='管理员'),
            'operator': OADepartment.objects.get(name='运维'),
            'test': OADepartment.objects.get(name='测试'),
            'general': OADepartment.objects.get(name='普通用户'),
            'developer': OADepartment.objects.get(name='研发'),
        }

        users = [
            {'email': 'admin@qq.com', 'realname': '管理员leader', 'password': '111111', 'department': 'admin',
             'is_superuser': True},
            {'email': 'operator@qq.com', 'realname': '运维leader', 'password': '111111', 'department': 'operator',
             'is_superuser': True},
            {'email': 'test@qq.com', 'realname': '测试leader', 'password': '111111', 'department': 'test',
             'is_superuser': True},
            {'email': 'developer@qq.com', 'realname': '研发leader', 'password': '111111', 'department': 'developer',
             'is_superuser': True},
            {'email': 'general_ceshi@qq.com', 'realname': '普通1', 'password': '111111', 'department': 'general',
             'is_superuser': False},
            {'email': 'admin_ceshi@qq.com', 'realname': '管理员1', 'password': '111111', 'department': 'admin',
             'is_superuser': False},
            {'email': 'operator_ceshi@qq.com', 'realname': '运维1', 'password': '111111', 'department': 'operator',
             'is_superuser': False},
            {'email': 'test_ceshi@qq.com', 'realname': '测试1', 'password': '111111', 'department': 'test',
             'is_superuser': False},
            {'email': 'developer_ceshi@qq.com', 'realname': '研发1', 'password': '111111', 'department': 'developer',
             'is_superuser': False},
        ]

        for user_data in users:
            department = departments[user_data['department']]
            if user_data['is_superuser']:
                user, created = OAUser.objects.get_or_create(
                    email=user_data['email'],
                    defaults={
                        'realname': user_data['realname'],
                        'password': user_data['password'],
                        'department': department,
                        'is_superuser': True,
                        'is_staff': True,
                        'status': 1
                    }
                )
            else:
                user, created = OAUser.objects.get_or_create(
                    email=user_data['email'],
                    defaults={
                        'realname': user_data['realname'],
                        'password': user_data['password'],
                        'department': department,
                        'is_superuser': False,
                        'is_staff': True
                    }
                )
            if created:
                user.set_password(user_data['password'])  # 确保密码被正确地加密保存
                user.save()

        self.stdout.write(self.style.SUCCESS('初始用户创建成功！'))
