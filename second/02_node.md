#**第二天笔记**
###**list介绍**
#####1.查看所有元素--遍历

	for i in arr:
		print i

#####**2.list相关函数介绍**
list是个自带函数，可以把字符串切割成列表

	print list('hello')

len函数，可以得到list的长度

	print len([1,2,3,4,5])

in判断某个函数是不是在list里

	print 'h' in list('hello')

range是一个常用的辅助函数，快速生成数字list

	print range(10)
	print range(3,10)

list交换赋值

	arr[0],arr[1] = arr[1],arr[0]
	print arr

list可以直接相加
	
	arr1 = [1,2,3]
	arr2 = [4,5,6]
	print arr1+arr2

#####**3.list的操作，主要是增删改查**

	arr = [1,2,3]   
	增加:arr[1:1] = [6](用切片的方法)  
		 arr.append(4)(用append追加的方法)  
		 arr.insert(1,'raopeng')(用insert插入的方法)  
	删除:del arr[1]/arr.remove('1')/arr.pop(0)/arr[1:2] = [](用切片模拟)  
	修改:arr[0] = 'a'/arr[1:2] = ['a'](用切片模拟)  
	查询:in判断元素是否存在  
		 for遍历/arr[2](知道索引值，直接查询)  
		 print arr[0:3](切片模拟)  
		 count print arr.count(1)(统计1出现的次数)  
		 index print arr.index(2)(得到元素2的索引值)  
	其它:reverse   
		 arr.reverse();print arr(反转list)  

#####**4.list的代码小例子**
`例子1:让用户输入一个数组，如何最快的找到用户输入数字的索引`  

	方法用二分查找  
	伪代码:  
		先拿出数组中间的数mid，和输入比较  
		如果比mid大，就再后面一半数组，继续折半查找  
		如果比mid小，就在前面的数组，折半查找  
	arr = [1,3,7,10,22,100,299,1000,2000,30000,40000]
	num_to_find = 3
	start = 0
	end = len(arr)-1
	while True:
		mid = (start+end)/2
		mid_num = arr[mid]
		if mid==start:
		    print 'can not find,should after %s=>%s'%(start,arr[start])
			break
		print start,end,mid
		if num_to_find<mid_num:
			end = mid
		elif num_to_find>mid_num:
		    start = mid
		else:
			print 'find',mid
			break
		print start,end,id

`例子2:冒泡排序`

	arr = [3,100,111,7,18,2,20,99,1,54,33,8]
	count = 0
	for j in range(len(arr)-1):
		for i in range(len(arr)-1-j):
			count += 1
			if arr[i]>arr[i+1]:
				arr[i],arr[i+1]=arr[i+1],arr[i]
	print count
	print arr

###**字符串介绍**
#####**操作**
1.字符串可以+和*

	print 'hello'+'world'
	print '*'*40

2.split把字符串切割为list

	print 'hello,world,rp'.split(',')

3.join把list拼接成字符串

	print ','.join(['hello','world','rp'])

4.replace替换字符串的分割符

	print 'hello,wor,ld'.replace(',','||')
	my_str = 'hello,world:you,xxx,xxx:xxx'
	print 'hello,reboot:you,xxx,xxx::xxx'.replace(':',',').split(',')

5.字符串也是类数组的数据结构，但是不可修改，只能返回结果

	name = 'hello'
	print name[0]
	print name[-1]
	print name[1:4]
	for n in name:
		print n

