#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-


from sshtunnel import SSHTunnelForwarder # ssh连接库
import redis


# pool = redis.ConnectionPool(host='172.18.110.126', port=6379,password='Watone1234',db=2,decode_responses=True)
# #pool = redis.ConnectionPool(host='r-q0u0578e140ea9b4.redis.rds.wtops-procloud.com', port=6379,db=2,password='Watone1234',decode_responses=True)
# r = redis.Redis(connection_pool=pool)
# r.set('name', 'runoob')  # 设置 name 对应的值
# print(r['name'])
# print(r.get('Customer-user:1807'))  # 取出键 name 对应的值
# print(type(r.get('Customer-user:1807')))  # 查看类型

class Redis_token():

    def __init__(self,host,port,password=None,db=None):
        self.pool = redis.ConnectionPool(host=host, port=port, password=password, db=db,
                                              decode_responses=True)
        self.r = redis.Redis(connection_pool=self.pool)

    def token_values_jierufang(self,usid):
        token = self.r.get('Customer-user:%s' %usid)
        return token
    def token_values_yunying(self,usid):
        token = self.r.get('Operation-user:%s' %usid)
        return token






class Token_userid():
    def __init__(self,sship=None,sshname=None, sshpassword=None,redisip=None,redisbind=None):
        self.sship=sship
        self.sshname=sshname
        self.sshpassword = sshpassword
        self.redisip=redisip
        self.redisbind=redisbind

    def token_values_jierufang(self,userid):
        with SSHTunnelForwarder(
                (self.sship,22),  # 跳板机
                ssh_username=self.sshname,
                ssh_password=self.sshpassword,
                remote_bind_address=(self.redisip, self.redisbind),  # 远程的Redis服务器
                local_bind_address=('0.0.0.0', 10022)  # 开启本地转发端口
        ) as server:
            server.start()
            # print(server.local_bind_port)
            pool = redis.ConnectionPool(host='127.0.0.1', port=server.local_bind_port, db=0, decode_responses=True)
            red = redis.Redis(connection_pool=pool)
            token = red.get('Customer-user:%s' %userid)
            server.close()
            return token

    def token_values_yunying(self,userid):
        with SSHTunnelForwarder(
                (self.sship,22),  # 跳板机
                ssh_username=self.sshname,

                ssh_password=self.sshpassword,
                remote_bind_address=(self.redisip, self.redisbind),  # 远程的Redis服务器
                local_bind_address=('0.0.0.0', 10022)  # 开启本地转发端口
        ) as server:
            server.start()
            # print(server.local_bind_port)
            pool = redis.ConnectionPool(host='127.0.0.1', port=server.local_bind_port, db=0, decode_responses=True)
            red = redis.Redis(connection_pool=pool)
            token = red.get('Operation-user:%s' %userid)
            server.close()
            return token


if __name__ == '__main__':
    # rt = Redis_token('172.16.147.65', 6379, db=0)
    # print(rt.token_values_jierufang(775))
    tu = Token_userid(sship='47.111.237.77',sshname='root',sshpassword='Nice@1994',redisip='172.16.147.65',redisbind=46379)
    print(tu.token_values_jierufang(822))

