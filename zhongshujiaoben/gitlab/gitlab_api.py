#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
import requests
import json
import gitlab

url = 'https://gitlab2.cspiretech.com/users/sign_in'
token = 'uLkbbj_XtMwN8Sx2t82w'

# 登录
# gl = gitlab.Gitlab('https://gitlab2.cspiretech.com', private_token='uLkbbj_XtMwN8Sx2t82w')
# 列出所有的项目
# 列出所有的组
# all_groups = gl.groups.list(all=True)
# print(all_groups)
# for group in all_groups:
    # print(group.name,group.id)
# 获取所有的project
# projects = gl.projects.list(all=True)

# 获取所有的用户列表
# users = gl.users.list(all=True)
# print(users)
# zc=gl.users.get(154)
# print(zc.name)

# def assgroup():
    #######获取gitlab指定组内所有user以及project名称以及ID信息，本例中组ID为58###
    # gid = int(input('Input the group ID: '))
    # group = gl.groups.get(gid)
    # print(group.name)
    # members = group.members.list(all=True)
    # for me in members:
    #    print (me.username,me.id)
    # projects = group.projects.list(all=True)
    # for project in projects:
    #     print (group.name,project.name)

# print(assgroup())


#列出对组或项目的访问请求
def gitlab_groups():
    url='https://gitlab2.cspiretech.com/api/v4/groups/?%d/access_requests' %(191)
    header={"PRIVATE-TOKEN":"uLkbbj_XtMwN8Sx2t82w"}
    res=requests.get(url,headers=header)
    # res.content.decode("utf-8")
    return res.json()
print(gitlab_groups())

def gitlab_children():
    url='https://gitlab2.cspiretech.com/api/v4/projects/?id=622&/access_requests'
    header={"PRIVATE-TOKEN":"uLkbbj_XtMwN8Sx2t82w"}
    # data={
    #     "id":722
    # }
    res=requests.get(url,headers=header)
    return res.json()
# print(gitlab_children())



#批准访问请求
def gitlab_request_groups():
    url='https://gitlab2.cspiretech.com/api/v4/groups/?%d/access_requests/%d/approve?access_level=30' %(407,93)
    header={"PRIVATE-TOKEN":"uLkbbj_XtMwN8Sx2t82w"}
    # data = {
    #     "id":622, #service_operation
    #     "user_id":93, #授权用户
    #     "access_level":30  #授权类型  开发
    # }
    res=requests.put(url,headers=header)
    return res.json()
# print(gitlab_request_groups())

# curl --request PUT --header "PRIVATE-TOKEN: <uLkbbj_XtMwN8Sx2t82w>" "https://gitlab2.cspiretech.com/api/v4/groups/116/access_requests/93/approve?access_level=20"
# curl --request PUT --header "PRIVATE-TOKEN: <uLkbbj_XtMwN8Sx2t82w>" "https://gitlab2.cspiretech.com/api/v4/projects/622/access_requests/93/approve?access_level=20"
