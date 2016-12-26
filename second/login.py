#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   author:RaoPeng

#用户的登录信息存储形式是：用户名:密码
#让用户输入用户名和密码，判断能否登录

#函数功能：判断用户输入的账号和密码是否正常
#函数返回值：返回登录的提示信息，如：login成功
def check_login(arr,username,pwd):
	user_dict = {}
	for i in arr:
		tmp = i.split(':')
		user_dict[tmp[0]] = tmp[1]
	if username in user_dict and pwd==user_dict[username]:
		return 'login success!!!'
	elif username in user_dict and pwd!=user_dict[username]:
		return 'password is wrong!!!'
	elif username not in user_dict:
		return 'username not exits!!!'

input_username = raw_input('请输入用户名: ')
input_pwd = raw_input('请输入密码: ')
arr = ['rp:123','wkk:456','xiaoming:789']
print check_login(arr,username=input_username,pwd=input_pwd)

