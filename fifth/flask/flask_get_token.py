#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  author:RaoPeng

from flask import Flask,request,render_template,redirect
import get_token
app = Flask(__name__)

@app.route('/token')
def token():
	aid = request.args.get("appid")
	asecret = request.args.get("appsecret")
	agrant = 'client_credentials'
	res = get_token.get_t(appid=aid,appsecret=asecret,grant_type=agrant)
	return render_template('token.html',token=res)

if __name__=='__main__':
	app.run(host='0.0.0.0',port=10008,debug=True)
