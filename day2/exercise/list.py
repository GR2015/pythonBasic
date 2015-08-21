#方法1
lista=[4,3,6]
i=1
n=len(lista)
while i<n:
  lista[i]+=lista[i-1]
  i+=1

lista

#方法2
lista=[4,3,6]
num=0
for idx,i in enumerate(lista):
  print num,idx
  num+=i
  lista[idx]=num

print lista


#不改变原列表
a=[4,3,6]
b=[]
num=0
for index,i in enumerate(a):
  num+=i
  b.append(num)
print b

#[1,2,3，4,5,6] 变为[0,1,3，6,10,15]

a=[1,2,3,4,5,6]
new=[]
num=0
for index,i in enumerate(a):
  new.append(num)
  num+=a[index]
  print index,i,num

print new 

#奇数变平方，偶数不变[1,2,3,4,8,7,22,23]
lista=[1,2,3,4,8,7,22,23]
listb=[]
for i in lista:
  if i%2==0:
    listb.append(i)
  else:
    listb.append(i**2)

print listb



list =[1,2,3,4,8,7, 22,33, 88]
    list1=[]
    for i in list:
        if (i%2) != 0:#或者for i%2==1
            i=i*i
            list1.append(i)
        else :
            list1.append(i)
    print list1



a=['abc','efg','hij']
for i in a:
   for j in i:
    print i,j



#****打印4*4正方形
for i in range(4):
  for j in range(4):
    print '*',
  print ""    


*
**
***
****
n=4
for i in range(n):
  for j in range(i+1):
    print '*',
  print ""    


打印口图形
n=2
**
**

n=2
for i in range(n):
  print '*'*n,
  print ""    

打印X图形
n=3
* * 
 *  
* * 

0,0 0.1 0,2
1,0 1,1 1,2
2,0 2,1 2,2

x=y
x+y=2

n=3
for i in range(n):
  for j in range(n):
    if i==j:
      print "*",
    elif i+j==n-1:
      print "*",
    else:
      print " ",
  print "\n"

#如果在print末尾加逗号的话，是不会输出回车了，但是会自动输出一个空格
#用格式控制，print "%d%s" % (12,'world')
#本题中不打*坐标打印出三个空格

n=4
*  *
 ** 
 **
*  *

0,0         0,3
    1,1 1,2  
    2,1 2,2 
3,0          3,3


x=y
x+y=4

n=4
for i in range(n):
  for j in range(n):
    if i==j:
      print "*",
    elif i+j==n-1:
      print "*",
    else:
      print " ",
  print "\n"



a=[1,2,3]
b=[2,3,4]
c=[]
#1
for i in a:
  for j in b:
    if i==j:
      c.append(j)

print c


#2
>>> c=[]
>>> for i in a:
...   if i in b:
...     c.append(i)
...
>>> c
[2, 3]

for letter in 'python':
  if letter == 'h':
    break
  print 'current letter:',letter

所有元素and结果
a=[True,False.True,False]
c=True

for i in a:
  c = c and i

print c
    

所有元素or结果
a=[True,False.True,False]
c=False

for i in a:
  c=c or i

print c



s=raw_input('please input a number:\n')
t=int(s)
g=28

g=28
while (1):
  s=raw_input('please input a number:\n')
  t=int(s)
  if t > g:
    print 'bigger'
  elif t < g:
    print 'less'
  else:
    print 'right'
    break



#!/usr/bin/python
#coding=utf-8
import random

randNum = random.randint(1,100)
print "*****************猜数游戏开始*****************"
n = 0
while 1 :
  try :
    receiveNum = int(raw_input("please input a positive integer x："))
    print "\n"
  except :
    print "please input a positive integer!\nGame Over!!!"
  if receiveNum == randNum :
    print "Congratulation,You Win!!!"
    n += 1
    print "\nA total of %d steps" %(n)
    print "**********Game Over************"
    break
  elif receiveNum > randNum :
    print "Bigger!!!\nPlease try again!!!"
    n += 1
    continue
  else :
    print "Small!!!\nPlease try again!!!"
    n += 1
    continue

for idx,i in enumerate(x):

二分查找
x=[1,2,3,4,5,6,7,85,223]
find=3
idx =len(x)/2
x[idx] >find,  0-m-1
x[idx] < find   m- -1

128内猜7次
b=range(100)
find=44
idx=len(b)/2
for i in b:
  if b[idx]>find:
    print "bigger"
    idx=len(idx)/2
    continue
  elif b[idx]<find:
    print "less"
    idx=(len(idx)+len(idx)/2)/2
    continue
  else:
    print "right!"
    break
  
  
s='asdfbc'
aoeiu 
1. s 是否包含元字符，结果是True还是False
2. s是不是仅由元字符组成？
aoe
True

#1
a=False
s='asdfbc'
for i in s:
  if i in 'aoeiuAOEIU':
    a=True
    break
  else:
    a=False

print a

#2
flag=False
s='asdfbc'
for i in s:
  if i not in 'aoeiuAOEIU':
    flag=True
    break
  else:
    flag=False
    continue

if flag==True:
  print "not only aoeiuAOEIU"
else:
   print "only aoeiuAOEIU"





#计数
#s=raw_input("please enter:")


s='asADAfdsfdsafdsaf123233223'
lcount=dcount=scount=ocount=0
for i in s:
  if ord(i)>=65 and ord(i)<=122:
   lcount+=1
  elif ord(i)>=48 and ord(i)<=57:
   dcount+=1
  elif ord(i)==32:
   scount+=1
  else:
   ocount+=1

print "number of letter is %d \nnumber of digital is %d \nnumber of space is %d \nnumber of other is %d" %(lcount,dcount,scount,ocount)


if ch >='a' and ch <='z' or ch >='A' and ch <='Z'

if ch >='0' and ch <='9'

检查密码

passwd='dsfaf12'

强 >=8  并且 密码包含字母和数字
中 >=8, 或者包含字母，或者数字
弱 <8 ，包含字母或者数字

密码强度第二题：
c1 : 长度>=8
c2: 包含数字
c3: 包含！@#￥%

强：满足c1,c2,c3
中: 满足2个条件
弱：满足条件
弱：满足1个条件

s=raw_input("please enter:")
if len(s)>=8:
  for i in s:
    if ((i >='a' and i <='z' or i >='A' and i <='Z') and (i >='0' and i <='9')):
      print "high"
    elif ((i >='a' and i <='z' or i >='A' and i <='Z') or (i >='0' and i <='9')):
      print "media"
else:
    if (i >='a' and i <='z' or i >='A' and i <='Z') or (i >='0' and i <='9'))
      print "low"

s='dsfaf12234' 
if len(s)>=8: 
  for i in s:   
    if ((i >='a' and i <='z' or i >='A' and i <='Z') or (i >='0' and i <='9')):
      if ((i >='a' and i <='z' or i >='A' and i <='Z') and (i >='0' and i <='9')):
        print "high"
      else:
         print "media"




1、循环遍历词典d，得到当前的k，v
2 、 之前有没有出现过，如出现了sd[v] +=1 ,如果没出现，sd[v]=1
3、print sd

d={'a':1,'b':2,'c':1,'d':3}
sd={}
for k,v in d.items():
  if sd.has_key(v):
    print sd
    sd[v]+=1
  else:
    sd[v]=1

print sd
       
      

作业：
【冒泡】谢老师
打印N，口的图案
12、作业3 剩余部分
2分查找
【冒泡】谢老师 2015/8/15 17:44:56
day2\hw1.py
day2\hw2.py
day2\hw3.py

c=a and b

















  

