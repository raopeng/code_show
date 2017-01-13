#!/usr/bin/env python
#  -*- coding:utf-8 -*-
#    author:RaoPeng

from flask import Flask,request,render_template,redirect,session
from fileutil import read_user,add_user,mod_user,del_user
from check_user import check
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
@app.route('/login')
def login():
	user = request.args.get("user")
	pwd = request.args.get("password")
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
	#user_dict = read_user()
	if 'username' in session:
		return render_template('userinfo.html',udict=read_user())
	else:
		return redirect('/')

#添加新用户
@app.route('/adduser')
def add_u():
	user = request.args.get("user")
	pwd = request.args.get("password")
	res_msg = add_user(user=user,pwd=pwd)
	return redirect('/userinfo')

#删除用户
@app.route('/deluser')
def del_u():
	user = request.args.get("user")
	del_user(user=user)
	return redirect('/userinfo')

#更新用户
@app.route('/updateuser')
def update_u():
	user_dict = read_user()
	user = request.args.get("user")
	pwd = user_dict[user]
	return render_template('update.html',pwd=pwd,user=user)
@app.route('/updateaction')
def updateaction():
	user = request.args.get("user")
	pwd = request.args.get("new_pwd")
	mod_user(user=user,pwd=pwd)
	return redirect('userinfo')

if __name__=='__main__':
	app.run(host='0.0.0.0',port=10009,debug=True)

