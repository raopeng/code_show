#!/usr/bin/env python
# -*- coding: utf-8 -*-
#    author:RaoPeng

from flask import Flask,request,render_template,redirect,session
import MySQLdb as mysql
import json

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

conn = mysql.connect(user='xxx',passwd='123456',host='x.x.x.x',db='xxx')
conn.autocommit(True)
cur = conn.cursor()
#cur.execute('select * from raopeng_user')
#print cur.fetchall()

@app.context_processor
def inject_user():
	return {'username':'raopeng'}

@app.route('/idc')
def idc():
	return render_template('idc.html')

@app.route('/idclist')
def idclist():
	cur.execute('select * from idc')
	res = cur.fetchall()
	return json.dumps(res)

@app.route('/addidc',methods=['post'])
def addidc():
	idc_name = request.form.get('name')
	sql = 'insert into idc (name) values ("%s")'%(idc_name)
	print sql
	cur.execute(sql)
	return 'ok'

@app.route('/server')
def server():
	return render_template('server.html')

@app.route('/serverlist')
def serverlist():
	cur.execute('select * from pc')
	res = cur.fetchall()
	return json.dumps(res)

@app.route('/addserver',methods=['post'])
def addserver():
	ip = request.form.get('ip')
	mem = request.form.get('mem')
	idc_id = request.form.get('idc_id')
	create_time = request.form.get('create_time')
	sql = 'insert into pc (ip,mem,idc_id,create_time) values ("%s",%s,%s,"%s")'%(ip,mem,idc_id,create_time)
	cur.execute(sql)
	return 'ok'

@app.route('/delserver',methods=['post'])
def delserver():
	id = request.form.get('id')
	if not id:
		return 'error'
	sql = 'delete from pc where id=%s'%(id)
	cur.execute(sql)
	return 'ok'

if __name__=='__main__':
	app.run(host='0.0.0.0',port=10008,debug=True)
