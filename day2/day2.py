#����м�λ�õĹؼ�������ҹؼ��ֱȽϣ������ɹ������������м�λ�ý����Ϊǰ�������ֱ�
#����м�λ�õĹؼ��ִ��ڲ��ҹؼ��֣����һ������ǰһ���ֱ������һ�����Һ�һ���ֱ�
#�ظ�������̣�ֱ���ҵ����������ļ�¼��ʹ���ҳɹ�����ֱ���ӱ�����Ϊֹ����ʱ���Ҳ��ɹ�
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
#s�Ƿ����Ԫ�ַ����Ƿ����Ԫ�ַ����
s="aeiouAEIOU"
u="aeiou"
flag=0
for i in u:  
	if i not in s:  
		print '��ȫ��Ԫ����ĸ���'
		flag=1
		break
	elif flag==0:  
		print '����Ԫ����ĸ'
else:  
	print '������Ԫ����ĸ'	
	
	
#coding=utf-8
#��ӡN�ͣ�����ͼ��
#i��j�У���1�У��͵�5��ʱ�����*����i=jʱ�����*
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
#�б����
#����һ������
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
#x&y��
#x|y��
#x-y��
#ret = list(set(a) ^ set(b))
#print list(set(a).union(set(b)))
#print list(set(b).difference(set(a))) # b���ж�a��û�е�
for i in x:  
	if i in y:  
	  a.append(i)#��
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

����ǿ�ȵڶ��⣺
c1 : ����>=8
c2: ��������
c3: ������@#��%

ǿ������c1,c2,c3
��: ֻ����2������
����ֻ����1������

c2='1234567890'
c3='!@#%' 
if len(pw)>=8:  
  if pw in c2,c3
    print 'ǿ����'
  else:  
    print '������'
print '������' 




