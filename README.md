## 开发中......
## 运行方法
### 1.安装依赖
`pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple`
### 2.修改oa_back下的settings中的mysql相关配置
### 3.数据库创建和迁移
`create database oa_project;`

shell终端执行数据库迁移`python manage.py makemigrations`和`python manage.py migrate`

继续在shell终端执行数据初始化操作：
`python .\manage.py init_departments`
`python .\manage.py init_menu`
`python .\manage.py init_user`

### 4.运行即可