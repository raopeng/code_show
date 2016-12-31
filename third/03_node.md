#**第三天笔记**
###**元祖介绍**
1.除了修改，所有数组的属性都有
2.不可修改，所以速度快
3.可以当做dict的key，而list不行
4.形式：tup = (1,2,3)
###**字典介绍**
#####**1.字典表示形式**

	my_dict = {
		(12,1,2):'tuple',
		0:'test0',
		'name':'rp',
		'age':12,
		'hobby':['linux','python'],
		'des':{
			'job':'ops',
			'sex':'man'
		}
	}

#####**2.字典的特点**
	`字典里的数据没有顺序，查找迅速，dict里面有1个数据还是10万个数据，查找速度基本一样，是key:value的形式，key必须是不可变的数据结构，value任意`
#######**2-1.字典的增删改查**

	`my_dict = {'name':'rp','age':12}`
	.`增加:`

		my_dict['job'] = 'ops']
		print my_dict

	.`删除:`

		清空所有:
			my_dict.clear()
			my_dict = {}
		清空某个key的value:
			my_dict['name'] = ''
		删除某个key:
			del my_dict['age']
			print my_dict

	.`修改:`
		
		my_dict['name'] = 'hello'
		print my_dict

	.`查询:`
		
		print my_dict['name']

#######**2-2.字典in的用法**

	.`in判断字典是否有这个key`

		print 'name' in my_dict

	.`len获取dict中的数据数量`

		print len(my_dict)

	.`用for循环来遍历字典的key`
		
		for k in my_dict:
			print 'key:%s---------->value:%s' %(k,my_dict[k])

	
