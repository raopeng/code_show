#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  author:RaoPeng

import json
import time
import requests

def get_t(**kargs):
	token_url = 'https://cdncs-api.fastweb.com.cn/oauth/access_token'
	token_json = requests.post(token_url,data=json.dumps(kargs))
	token_res = json.loads(token_json.text)['result']['access_token']
	print token_res
	return token_res

if __name__=='__main__':
	print get_t(appid='1fe358385e0748b1ef3f50aafc4463',appsecret='40537f411f',grant_type='client_credentials')

