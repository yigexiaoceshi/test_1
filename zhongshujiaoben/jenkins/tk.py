#!/usr/local/bin python3.7
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox

#打包配置项
#Jenkins地址
jenkins_url='http://172.18.39.86:8080/'
jenkins_username='zhouchengjie'
jenkins_password='yunyang@zcj'



root = Tk()
root.title("打包窗口")
root.geometry('800x400')  # 是x 不是*


#窗口一
l1 = Label(root, text="工程名:").place(x=30,y=20)
# l1.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
xls_text = StringVar()
xls = Entry(root, textvariable=xls_text).place(x=80,y=20)
xls_text.set("")
# xls.pack()

l2 = Label(root, text="分支名:").place(x=30,y=50)
# l2.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
sheet_text = StringVar()
sheet = Entry(root, textvariable=sheet_text).place(x=80,y=50)
sheet_text.set("")

#窗口二
l3 = Label(root, text="工程名:").place(x=280,y=20)
# l1.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
xls_text01 = StringVar()
xls01 = Entry(root, textvariable=xls_text01).place(x=330,y=20)
xls_text.set("")
# xls.pack()

l4 = Label(root, text="分支名:").place(x=280,y=50)
# l2.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
sheet_text01 = StringVar()
sheet01 = Entry(root, textvariable=sheet_text01).place(x=330,y=50)
sheet_text.set("")
# sheet.pack()

#窗口三
l5 = Label(root, text="工程名:").place(x=530,y=20)
# l1.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
xls_text02 = StringVar()
xls02 = Entry(root, textvariable=xls_text02).place(x=580,y=20)
xls_text.set("")
# xls.pack()

l6 = Label(root, text="分支名:").place(x=530,y=50)
# l2.pack()  # 这里的side可以赋值为LEFT  RTGHT TOP  BOTTOM
sheet_text02 = StringVar()
sheet02 = Entry(root, textvariable=sheet_text02).place(x=580,y=50)
sheet_text.set("")
# sheet.pack()

number = Label(root, text="打包数量:").place(x=30,y=85)
sheet_number = StringVar()
number_01 = Spinbox(root,from_=1,to=3,wrap=False,textvariable=sheet_number).place(x=100,y=85,width=40, height=25)
sheet_number.set("1")
# sheet.pack()



# l1.grid(row=0, column=0)
# xls.grid(row=0, column=1)
# l2.grid(row=0, column=0)
# sheet.grid(row=0, column=1)
# l1.place(x=20,y=10)
# xls.place(x=20,y=30)
# l2.place(x=20,y=50)
# sheet.place(x=20,y=70)




v = IntVar()
v.set(1)
vv=Radiobutton(root, text='test版本', variable=v, value=1,).place(x=30,y=120)
vv1=Radiobutton(root, text='release版本', variable=v, value=2,).place(x=30,y=140)


M=IntVar()
M.set(1)
mm=Radiobutton(root, text='测试环境rancher', variable=M, value=1,).place(x=30,y=170)
mm1=Radiobutton(root, text='演示环境rancher', variable=M, value=2,).place(x=30,y=190)

t_number = Label(root, text="是否发布tag：").place(x=150,y=120)
j=IntVar()
j.set(2)
jj=Radiobutton(root, text='是', variable=j, value=1).place(x=240,y=120)
jj1=Radiobutton(root, text='否', variable=j, value=2).place(x=240,y=140)

b2=Button(root, text="确定", command=root.destroy).place(x=30,y=240)
b3=Button(root, text="取消", command=sys.exit).place(x=100,y=240)
# console_text =Text(root, fg="green", bg="black", width=40, height=20, state=DISABLED)





# 定义变量
# v = StringVar()
#
# def callCheckbutton():
#     return  v.get()
#
# # 添加复选框
# c = Checkbutton(root,variable=v,
#             text='是否发布tag',
#             onvalue=1,  # 设置On的值，勾选返回1
#             offvalue=0,  # 设置Off的值
#             command=callCheckbutton).place(x=150,y=140)
# v.set('0')
# ss=v.get()
# print(ss)
# c.pack()

root.mainloop()




#工程前缀
name='centralsystem-'

gongchengming00=xls_text.get()
gongchengming01=xls_text01.get()
gongchengming02=xls_text02.get()

#自动清除空格
gongchengming_name=name+gongchengming00.strip()
gongchengming_name01=name+gongchengming01.strip()
gongchengming_name02=name+gongchengming02.strip()

fenzhi_a=sheet_text.get()
fenzhi001_a=sheet_text01.get()
fenzhi002_a=sheet_text02.get()

fenzhi=fenzhi_a.strip()
fenzhi001=fenzhi001_a.strip()
fenzhi002=fenzhi002_a.strip()

list=[gongchengming_name,gongchengming_name01,gongchengming_name02]
list005=[gongchengming00.strip(),gongchengming01.strip(),gongchengming02.strip()]
fenzhi_list=[fenzhi,fenzhi001,fenzhi002]

#打包数量
num=sheet_number.get()




nn=v.get()

mmm=M.get()

jt=j.get()


if jt==1:
    l_num=1
else:
    l_num=2


#版本号前缀
def bbb():
    if nn == 1:
        aas = "api"
        return aas
        # print(aas)
    elif nn == 2:
        bbs = "release-4.8."
        return bbs
        # print(bbs)

#选择的版本
def ssss():
    if nn ==1:
        aas="test_1.0."
        return aas
        # print(aas)
    elif nn==2:
        bbs="release-4.8."
        return bbs
        # print(bbs


def mmmm():
    if mmm ==1:
        #测试环境rancher地址
        aas="https://172.18.109.174/"
        username="admin"
        password="2cJSAnhLB75NDzxT"
        rancher_name="测试环境"
        return aas,username,password,rancher_name
        # print(aas)
    elif mmm==2:
        #演示环境rancher地址
        bbs="https://47.114.45.239/"
        username="admin"
        password="j45t^RrS5v@KugZO"
        rancher_name="演示环境"
        return bbs,username,password,rancher_name




# list22=[]
# aas="test_1.0.33"
# bbs="release-4.6.55"
# test_fenzhi = bbs.split('.')[2:]
# print(test_fenzhi)
#
# zhuanhuan = (','.join(test_fenzhi))
# list22.append(zhuanhuan)
# print(list22)
# # str转换int
# results = list(map(int, list22))
# max_num = max(results) + 1
# print(max_num)
# new_fenzhi = ssss() + str(max_num)
#
# print(new_fenzhi)




# def on_click():
#     x = xls_text.get()
#     s = sheet_text.get()
#     string = str("工程名：%s ，分支名：%s  " % (x, s))
#     print("工程名：%s ，分支名：%s " % (x, s))
#     messagebox.showinfo(title='aaa', message=string)
#     return x,s
#
# b1=tk.Button(root, text="确定", command=on_click).pack()
# root.mainloop()


