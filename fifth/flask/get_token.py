#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  author:RaoPeng

import json
import time
import requests

def get_t(**kargs):
	token_url = 'https://xxx.com/xxx/xxx'
	token_json = requests.post(token_url,data=json.dumps(kargs))
	token_res = json.loads(token_json.text)['result']['access_token']
	print token_res
	return token_res

if __name__=='__main__':
	get_t()
