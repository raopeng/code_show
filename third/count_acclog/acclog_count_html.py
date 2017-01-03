#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   author:RaoPeng

#需求:按照ip和访问状态两个维度统计数据，打印前十名，并且以html表格的形式展现
#补充html知识:
#        html 表格标签，html是前端使用的标记语言
#        html的表格标签都是成对出现的，需要闭合
# 语法:
#        <table></table>表格
#        <tr></tr>是一行，要在两个table标签中间
#        <td></td>是一个单元格，要在tr里

#不用函数的方式:

f = open('www_access_20140823.log')
dic = {}
res_dic = {}
for line in f:
	temp = (line.split(' ')[0],line.split(' ')[8])
	dic[temp] = dic.get(temp,0)+1

#反转dic,把出现的次数当成key
for k in dic:
	res_dic[dic[k]] = res_dic.get(dic[k],[])+[k]

#排序，取前十，在这里还是采用冒泡排序
count_arr = res_dic.keys()
for i in range(10):
	for j in range(len(count_arr)-1):
		if count_arr[j]>count_arr[j+1]:
			count_arr[j],count_arr[j+1] = count_arr[j+1],count_arr[j]

f = open('acclog.html','a')
f.write("<table border='1'>\n\t<tr>\n\t\t<td>IP</td>\n\t\t<td>STATUS</td>\n\t\t<td>COUNT</td>\n\t</tr>")
count = 0
while count<10:
	val = count_arr.pop()
	for k in res_dic[val]:
		f.write("\n\t<tr>\n\t\t<td>%s</td>\n\t\t<td>%s</td>\n\t\t<td>%s</td>\n\t</tr>" %(k[0],k[1],val))
		count +=1

f.close()
f.close()
