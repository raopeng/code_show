#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   author:RaoPeng

import MySQLdb as mysql

def my_sql(sql_str):
	conn = mysql.connect(user='woniu',passwd='123456',host='59.110.12.72',db='reboot12')
	conn.autocommit(True)
	cur = conn.cursor()
	cur.execute(sql_str)
	return cur.fetchall()

if __name__=='__main__':
	print my_sql(sql_str='select user,pwd from raopeng_user')
