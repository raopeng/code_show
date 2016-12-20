#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   author:RaoPeng

#数组去重(一个坑：最好不要在循环内部改变list的长度)

#一：正常的demo
arr = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
after_arr = []
for i in arr:
	if i not in after_arr:
		after_arr.append(i)
print after_arr

#二：遇到坑的demo
arr = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
#print arr
#print '+'*50
for i in arr:
	while True:
		if arr.count(i)==1:
			break
		else:
			arr.remove(i)#在这其实是已经修改了list的长度了
print arr #结果发现12还是出现了两次

#三：修改为函数版
#函数功能：数组去重
def lose_repeat_num(arr):
	after_arr = []
	for i in arr:
		if i not in after_arr:
			after_arr.append(i)
	return after_arr

arr = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
print lose_repeat_num(arr)
