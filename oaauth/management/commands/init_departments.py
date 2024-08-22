# -*- coding: utf-8 -*-
# @Time    : 2024-06-17 2:10
# @Author  : 子非鱼
# @File    : init_departments.py
# @Software: PyCharm
from django.core.management.base import BaseCommand

from oaauth.models import OADepartment


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # 初始化部门数据
        # 管理员
        admin = OADepartment.objects.create(name='管理员', intro="管理整个OA系统", depart_type=0)
        # 运维
        operator = OADepartment.objects.create(name='运维', intro="对工单进行审批等操作", depart_type=1)
        # 测试
        test = OADepartment.objects.create(name='测试', intro="发起工单", depart_type=2)
        # 普通用户
        general = OADepartment.objects.create(name='普通用户', intro="只具有查看权限", depart_type=3)
        # 研发
        developer = OADepartment.objects.create(name='研发', intro="查看一些研发相关的数据", depart_type=4)
        self.stdout.write('部门数据初始化成功！')
        # 使用python .\manage.py init_departments对数据进行插入数据库
