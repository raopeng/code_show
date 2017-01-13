#!/usr/bin/env python
#  -*- coding:utf-8 -*-
#   author:RaoPeng

#读文件函数
#返回值:用户信息字典
def read_file():
	user_dict = {}
	with open('user') as f:
		for i in f.read().split('\n'):
			if i=='':
				continue
			else:
				tmp = i.split(':')
				user_dict[tmp[0]] = tmp[1]
		return user_dict

#显示用户信息函数
#返回值:用户信息字典
def read_user():
	#user_dict = read_file()
	return read_file()

#添加用户信息函数
#返回值:用户已存在错误信息或用户信息字典
def add_user(user,pwd):
	add_msg = ''
	user_dict = read_file()
	if user in user_dict:
		add_msg = 'User:%s alredy exists!!!' %(user)
		return error_msg
	else:
		with open('user','a') as f:
			user_str = user+':'+pwd+'\n'
			f.write(user_str)
			add_msg = 'User:%s created successfully!' %(user)

#修改用户密码函数
#返回值:用户信息字典
def mod_user(user,pwd):
	user_dict = read_file()
	user_dict[user] = pwd
	with open('user','w') as f:
		for i in user_dict:
			user_str = i+':'+user_dict[i]+'\n'
			f.write(user_str)
		res_dict = read_file()

#删除用户函数
#返回值:用户信息字典
def del_user(user):
	user_dict = read_file()
	user_dict.pop(user)
	with open('user','w') as f:
		for i in user_dict:
			user_str = i+':'+user_dict[i]+'\n'
			f.write(user_str)

if __name__=='__main__':
	print read_user()
