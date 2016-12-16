#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   author:RaoPeng
arr = [3,7,18,2,20,10000,99,1,54,100,4,50,120,200,450]
count = 0
for i in range(len(arr)):
	for j in range(len(arr)-1-i):
		if arr[j]>arr[j+1]:
			arr[j],arr[j+1] = arr[j+1],arr[j]
		print arr
		print '='*50
		count += 1
print count
print arr
