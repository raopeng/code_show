#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   author:RaoPeng
for i in range(1,10):
	temp = ''
	for j in range(1,10):
		if i>=j:
			temp += '%s * %s = %s  ' %(i,j,i*j)
	print temp
