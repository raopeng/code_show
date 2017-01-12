#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   author:RaoPeng

def check(user,pwd):
	admin_user = {'admin':'admin'}
	if user in admin_user and admin_user[user]==pwd:
		return 0
	else:
		return 1

if __name__=='__main__':
	print check(user='admin',pwd='admin')
