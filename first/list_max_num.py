#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   author: RaoPeng
arr = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
max_num = 0
for i in arr:
	if i>max_num:
		max_num = i
print 'max num is %s' %(max_num)
