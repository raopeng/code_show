#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   author:RaoPeng
sum = 0
i = 0
while True:
	num = raw_input('please input a num:')
	if num == '':
		break
	i += 1
	sum += int(num)
print sum/i
