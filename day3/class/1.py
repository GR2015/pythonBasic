#coding=utf-8
'''def changeme(mylist):
  "�޸Ĵ�����б�"
  mylist.append([1,2,3,4])
  print "������ȡֵ��",mylist
  return'''
  
'''mylist=[10,20,30]
changeme(mylist)
print "������ȡֵ",mylist'''


'''def f(a)
  a=1
  #return a
  
a=2
f(a)
print a'''

def f(a,b,c,d):
  print a,b,c,d

y=f(1,2,3,4)
  
  
def printinfo(name,age=35):
   print "Name:",name
   print "Age:",age
   return'''

'''>>> printinfo(age=50,name="miki")
Name: miki
Age: 50
>>> printinfo(name="miki")
Name: miki
Age: 35
>>> printinfo('tom')
Name: tom
Age: 35
>>> printinfo('tom',15)
Name: tom
Age: 15'''

'''def printinfo(arg1,*vartuple):
  print "���"
  print arg1
  for var in vartuple:
    print var
  return

printinfo(10)
printinfo(70,60,50)



c=6
def print2(a,b,*d,**e):
  print a,b,c,d,e'''
  

def add(x,y):
  print x+y
  return
  
def sub(x,y):
  print x-y
  return
  
def multi(x,y):
  print x*y
  return
  
def div(x,y):
  if y==0:
    print "��������Ϊ0"
  else:
    print x/y
  return
  
add(10,5)
sub(10,5)
multi(10,5)
div(10,5)
div(1,0)

exp(x) ����e��x����(ex),
sqrt(x) ��������x��ƽ����

import math
def hw1(x):
  return x*math.exp(-x)+math.sqrt(1-math.exp(-x))
  
hw1(2)