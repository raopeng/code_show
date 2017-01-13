#!/usr/bin/env python
#  -*- coding:utf-8 -*-
#    author:RaoPeng

from flask import Flask,request,render_template,redirect,session
from check_user import check
from sqlutil import my_sql
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#渲染登录界面
@app.route('/')
def index():
	if 'username' in session:
		return redirect('/userinfo')
	else:
		return render_template('login.html')

#登录判断并跳转
@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=='GET':
		user = request.args.get("user")
		pwd = request.args.get("password")
	elif request.method=='POST':
		user = request.form.get("user")
		pwd = request.form.get("password")
	else:
		return redirect('/')
	error_msg = ''
	if user and pwd:
		if check(user=user,pwd=pwd)==0:
			session['username'] = 'admin'
			return redirect('/userinfo')
		else:
			error_msg = 'wrong user or password!'
	else:
		error_msg = 'the user name or password cannot be empty!'
	return render_template('login.html',error_msg=error_msg)

#登出操作
@app.route('/logout')
def logout():
	session.pop('username')
	return redirect('/')

#渲染显示用户信息页面
@app.route('/userinfo')
def show_user_info():
	sql_str = 'select user,pwd from raopeng_user'
	res = my_sql(sql_str)
	if 'username' in session:
		return render_template('userinfo.html',ulist=res)
	else:
		return redirect('/')

#添加新用户
@app.route('/adduser',methods=['GET','POST'])
def add_u():
	if request.method=='GET':
		user = request.args.get("user")
		pwd = request.args.get("password")
	else:
		user = request.form.get("user")
		pwd = request.form.get("password")
	sql_str = 'insert into raopeng_user values ("%s","%s")'%(user,pwd)
	my_sql(sql_str)
	return redirect('/userinfo')

#删除用户
@app.route('/deluser')
def del_u():
	user = request.args.get("user")
	sql_str = 'delete from raopeng_user where user="%s"'%(user)
	my_sql(sql_str)
	return redirect('/userinfo')

#更新用户
@app.route('/updateuser')
def update_u():
	user = request.args.get("user")
	sql_str = 'select user,pwd from raopeng_user where user="%s"'%(user)
	user_tup = my_sql(sql_str)
	pwd = user_tup[0][1]
	return render_template('update.html',pwd=pwd,user=user)
@app.route('/updateaction',methods=['GET','POST'])
def updateaction():
	if request.method=='GET':
		user = request.args.get("user")
		pwd = request.args.get("new_pwd")
	else:
		user = request.form.get("user")
		pwd = request.form.get("new_pwd")
	sql_str = 'update raopeng_user set pwd="%s" where user="%s"'%(pwd,user)
	my_sql(sql_str)
	return redirect('userinfo')

if __name__=='__main__':
	app.run(host='0.0.0.0',port=10009,debug=True)

