#如果中间位置的关键字与查找关键字比较，相等则成功，否则利用中间位置将表分为前后俩个字表
#如果中间位置的关键字大于查找关键字，则进一步查找前一个字表，否则进一步查找后一个字表，
#重复上面过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功
list=[2,3,4,5,6,80]
findnum=5
min=0
max=len(list)
while min<=max:  
	mid=(min+max)/2
	if findnum==list[mid]:  
		print mid
		break
	elif findnum<list[mid]:  
		mid=mid-1
	elif findnum>list[mid]:  
		mid=mid+1
		
		
		
#coding=utf-8
#aeiou
#s是否包含元字符，是否仅由元字符组成
s="aeiouAEIOU"
u="aeiou"
flag=0
for i in u:  
	if i not in s:  
		print '不全有元音字母组成'
		flag=1
		break
	elif flag==0:  
		print '包含元音字母'
else:  
	print '不包含元音字母'	
	
	
#coding=utf-8
#打印N型，口型图案
#i行j列，第1行，和第5行时都输出*，当i=j时，输出*
for i in range(5):  
	for  j in range(5):  
		if  j==0 or j==4:  
			print '*',
		elif i==j:  
			print '*',
		else:  
			print " ",
	print 		
	
	
	for i in range(5):  
	if i==0:  
		print '*  *  *  *  *',
	elif i==1:  
		print '*           *',
	elif i==2:  
		print '*           *',
	elif i==3:  
		print '*           *',
	elif i==4:  
		print '*  *  *  *  *',
	print
	
	
n=5
for i in range(n):  
	for j in range(n):  
		if i==0 or i==(n-1) or j==0 or j==n-1:  
			print '*',
		else:  
			print " ",
	print	
D:\>print.py
* * * * *
*       *
*       *
*       *
* * * * *	
	
#!/usr/bin/python
# -*- coding: utf-8 -*-
#列表求和
#定义一个数组
#sum[]
list1=[4,3,6]
list2=[]
sum=0
for i in list1:  
  sum=sum+i
  i=i+1
  list2.append(sum)
print list2
D:\>SUM.py
[4, 7, 13]



x=[2,3,4]
y=[3,4,5]
z=[]
a=[]
b=[]
#x&y交
#x|y并
#x-y差
#ret = list(set(a) ^ set(b))
#print list(set(a).union(set(b)))
#print list(set(b).difference(set(a))) # b中有而a中没有的
for i in x:  
	if i in y:  
	  a.append(i)#交
print a

D:\>no.py
[3, 4]
for i in x:  
	for j in y:  
	  if i not in y and j not in x:  
			z.append(i)
			z.append(j)
			break
print z
D:\>no.py
[2, 5]

print a+z


--[3, 4, 2, 5]

密码强度第二题：
c1 : 长度>=8
c2: 包含数字
c3: 包含！@#￥%

强：满足c1,c2,c3
中: 只满足2个条件
弱：只满足1个条件

c2='1234567890'
c3='!@#%' 
if len(pw)>=8:  
  if pw in c2,c3
    print '强密码'
  else:  
    print '中密码'
print '弱密码' 




