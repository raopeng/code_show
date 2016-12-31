#**第三天笔记**
###**元组介绍**
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
######**2-1.字典的增删改查**

	my_dict = {'name':'rp','age':12}
	a.增加:
		my_dict['job'] = 'ops']
		print my_dict
	b.删除:
		清空所有:
			my_dict.clear()
			my_dict = {}
		清空某个key的value:
			my_dict['name'] = ''
		删除某个key:
			del my_dict['age']
			print my_dict
	c.修改:	
		my_dict['name'] = 'hello'
		print my_dict
	d.查询:	
		print my_dict['name']

######**2-2.字典in的用法**

	in判断字典是否有这个key
		print 'name' in my_dict
	len获取dict中的数据数量
		print len(my_dict)
	用for循环来遍历字典的key	
		for k in my_dict:
			print 'key:%s---------->value:%s' %(k,my_dict[k])

######**2-3.字典get的用法**

	获取值my_dict.get(key,默认值)
		my_dict = {'name':'rp'}
		print my_dict.get('age',12)

######**2-4.字典fromkeys的用法**

	fromkeys快速从list转成一个dict
		print {}.fromkeys(['name','age'],'xxx')

######**2-5.字典keys,values的用法**

	my_dict = {'name':'reboot','type':'python'}
	keys获取字典key的list
		print my_dict.keys()
	values获取value的list
		print my_dict.values()

######**2-6.字典items,popitem的用法**

	items将字典的所有项以list的形式返回，list每一项是(key,value)
		print my_dict.items()
	popitem类似于list.pop,弹出一个随机的项
		print my_dict.popitem()
		print my_dict
	注:字典也有pop方法
		print my_dict.pop('name')

######**2-7.字典setdefault的用法**

	setdefault类似于get,可以设置默认值,并写入到原来的字典
		my_dict.setdefault('name1','xxx')
		print my_dict(发现name1写到字典里了)

###**文件处理**
#####**1.打开文件**
	
	open默认是读的打开方式,如果想写文件,要指明打开的模式,rwa
	f = open('test.txt')
	f = open('test.txt','w')
		'w'模式是覆盖的。w模式打开文件的时候，就把文件清空了
	f = open('user.txt','a')

#####**2.读取文件**

	read方法:
		read方法可以读取固定长度的字符,不传的话读到文件结束
		print f.read(5)
		print f.read()
	readline方法:
		readline一次读一行,指针移到行尾
		print f.readline()
	readlines方法:
		readlines一次全部读完,返回一个list,每行是一个元素,文件太大的时候不建议使用

#####**3.写文件**

	write方法:
		write将我们需要的字符当成参数传递就可以了,但是换行需要我们自己指定('\n'字符)
		f.write('test write sth\n')
	writelines方法:
		writelines传递给该函数一个字符串的list,它会把所有的字符串都写入文件,但是换行也需要我们自己指定('\n'字符)
		f.writelines(['xxx\n','ddd'])

#####**4.关闭文件**

		f.close()

