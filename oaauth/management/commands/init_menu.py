# -*- coding: utf-8 -*-
# @Time    : 2024-06-27 2:07
# @Author  : 子非鱼
# @File    : init_menu.py
# @Software: PyCharm
from django.core.management.base import BaseCommand

from oaauth.models import UserMenu


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # 初始化菜单数据
        # 管理员可见菜单
        admin_one = UserMenu.objects.create(name='后台面板', icon='Platform',
                                            child='[{"name": "主控台","icon": "Help","frontpath":"/"}]',
                                            permission_type=0)
        admin_two = UserMenu.objects.create(name='管理面板', icon='help',
                                            child='[{"name": "用户管理","icon": "home-filled","frontpath":"/user/list"}]',
                                            permission_type=0)
        admin_three = UserMenu.objects.create(name='工单面板', icon='List',
                                              child='[{"name": "工单列表(测试)","icon": "Tickets","frontpath":"/test_form/list"},{"name": "工单列表(运维)","icon": "Tickets","frontpath":"/ops_form/list"},{"name": "工单列表(普通)","icon": "Tickets","frontpath":"/normal/list"}]',
                                              permission_type=0)
        admin_four = UserMenu.objects.create(name='信息面板', icon='Checked',
                                             child='[{"name": "发布信息","icon": "SetUp","frontpath":"/publish/list"},{"name": "库表信息","icon": "Postcard","frontpath":"/database/list"}]',
                                             permission_type=0)
        operator_one = UserMenu.objects.create(name='后台面板', icon='Platform',
                                               child='[{"name": "主控台","icon": "Help","frontpath":"/"}]',
                                               permission_type=0)
        operator_two = UserMenu.objects.create(name='工单面板', icon='List',
                                               child='[{"name": "工单列表","icon": "Tickets","frontpath":"/ops_form/list"}]',
                                               permission_type=0)
        operator_three = UserMenu.objects.create(name='信息面板', icon='Checked',
                                                 child='[{"name": "发布信息","icon": "SetUp","frontpath":"/publish/list"},{"name": "库表信息","icon": "Postcard","frontpath":"/database/list"}]',
                                                 permission_type=0)
        test_one = UserMenu.objects.create(name='后台面板', icon='Platform',
                                           child='[{"name": "主控台","icon": "Help","frontpath":"/"}]',
                                           permission_type=0)
        test_two = UserMenu.objects.create(name='工单面板', icon='List',
                                           child='[{"name": "工单列表","icon": "Tickets","frontpath":"/test_form/list"}]',
                                           permission_type=0)
        test_three = UserMenu.objects.create(name='信息面板', icon='Checked',
                                             child='[{"name": "发布信息","icon": "SetUp","frontpath":"/publish/list"},{"name": "库表信息","icon": "Postcard","frontpath":"/database/list"}]',
                                             permission_type=0)
        general_one = UserMenu.objects.create(name='后台面板', icon='Platform',
                                              child='[{"name": "主控台","icon": "Help","frontpath":"/"}]',
                                              permission_type=0)
        general_two = UserMenu.objects.create(name='工单面板', icon='List',
                                              child='[{"name": "工单列表","icon": "Tickets","frontpath":"/normal/list"}]',
                                              permission_type=0)
        general_three = UserMenu.objects.create(name='信息面板', icon='Checked',
                                                child='[{"name": "发布信息","icon": "SetUp","frontpath":"/publish/list"},{"name": "库表信息","icon": "Postcard","frontpath":"/database/list"}]',
                                                permission_type=0)
        developer_one = UserMenu.objects.create(name='后台面板', icon='Platform',
                                                child='[{"name": "主控台","icon": "Help","frontpath":"/"}]',
                                                permission_type=0)
        developer_two = UserMenu.objects.create(name='工单面板', icon='List',
                                                child='[{"name": "工单列表","icon": "Tickets","frontpath":"/normal/list"}]',
                                                permission_type=0)
        developer_three = UserMenu.objects.create(name='信息面板', icon='Checked',
                                                  child='[{"name": "发布信息","icon": "SetUp","frontpath":"/publish/list"},{"name": "库表信息","icon": "Postcard","frontpath":"/database/list"}]',
                                                  permission_type=0)
        self.stdout.write('菜单数据初始化成功！')
        # 使用python .\manage.py init_menu对数据进行插入数据库
