#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import traceback

from sshtunnel import SSHTunnelForwarder
import pymysql
#打开数据库连接
# db=pymysql.connect("172.18.109.62","centralsystem","UaoUOru8A6K3","citybrain_servcie")  #注意：harset="utf8",中间没有空格，因为mySql不支持

# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# sql="select * from operation_user where login_name="api""
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute(sql)
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print("Database version : %s " % data)

# 关闭数据库连接
# db.close()

# with SSHTunnelForwarder(
#         ('121.199.40.154',8095),                    # 跳板机ip及端口
#         ssh_password='s2QXoPteYwpkaKyK',                 # 跳板机密码
#         ssh_username='yunyang',                    # 跳板机用户名
#         remote_bind_address=('172.16.147.112',13306)) as server:  # 连接的数据库地址及端口
#
#     db_connect = pymysql.connect(host='127.0.0.1',                 # 此处必须是是127.0.0.1
#                                  port=server.local_bind_port,      # 默认，无需修改
#                                  user='root',                      # 连接的数据库用户名
#                                  passwd='vvlXMcy9f!l&clbF',                  # 连接的数据库密码
#                                  db='centralsystem_service')                     # 连接的数据库名称
#     #创建游标
#     cursor=db_connect.cursor()
#
#     #sql语句必须要使用单引号，不能使用双引号
#     sql="select * from operation_user where user_id='3'"
#     sql01="select * from operation_user"
#     try:
#         # 使用 execute()方法执行SQL查询
#         cursor.execute(sql01)
#         # 提交到数据库执行
#         db_connect.commit()
#         #fetchall()表示输出当前SQL语句所有数据，fetchone()返回一条SQL数据；
#         data=cursor.fetchall()
#         # print(data)
#         print("执行成功！")
#         # login_name=data[1]
#         list=[]
#         # 遍历结果
#         for row in data:
#             # user_id = row[0]
#             login_name = row[1]
#             list.append(login_name)
#             # password = row[2]
#             # print(login_name)
#     except:
#         #输出准确的异常信息
#         traceback.print_exc()
#         #回滚SQL语句
#         db_connect.rollback()
#     finally:
#         #关闭连接
#         db_connect.close()
#
#
# print(list[2])



# from sshtunnel import SSHTunnelForwarder
# import pymysql
#
# # 通过SSH连接云服务器
# server = SSHTunnelForwarder(
# 	ssh_address_or_host=('121.199.40.154',8095),  # 云服务器地址IP和端口port
# 	ssh_username="yunyang",  # 云服务器登录账号admin
# 	ssh_password="s2QXoPteYwpkaKyK",  # 云服务器登录密码password
# 	remote_bind_address=('172.16.147.112',13306)  # 数据库服务地址ip,一般为localhost和端口port，一般为330
# )
#
# # 云服务器开启
# server.start()
# # 云服务器上mysql数据库连接
# con = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
#                       port=server.local_bind_port,
#                       user="root",  # mysql的登录账号admin
#                       password="vvlXMcy9f!l&clbF",  # mysql的登录密码pwd
#                       db="centralsystem_service",  # mysql中要访问的数据表
#                       charset='utf8')  # 表的字符集
# # 创建游标
# cur = con.cursor()
# # 执行sql语句
# cur.execute("""select * from operation_user""")
# # 读取数据
# data = cur.fetchall()
# # 打印数据
# for item in data:
#     print(item)
# # 游标、连接关闭
# cur.close()
# con.close()
# # 云服务器关闭
# server.close()

