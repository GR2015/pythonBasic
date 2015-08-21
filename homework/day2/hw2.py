# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 19:53:20 2015

@author: cindychen
"""

#对一个list的所有元素求and，or，not
list_a=[True,False,True,False]
list_or=[]
a=len(list_a)
s=True
for i in range(1,a):
    s=s and list_a[i]
print 'list(and) :',s

s=True
for i in range(1,a):
    s=s or list_a[i]
print 'list(or) :',s
    
  
for i in list_a:
    list_or.append(not i)
print 'list(or):',list_or
  


#对2个list的对应元素求and，or，生成结果list
list_c=[True,False,True,False]
list_d=[False,False,True,True]
num1=len(list_c)
num2=len(list_d)
list_and=[]
list_or=[]

for i in range(num1):
    for j in range(num2):
        if j==i:
            list_and.append(list_c[i] and list_d[j])
            list_or.append(list_c[i] or list_d[j])
            
print 'list_and:',list_and
print 'list_or:',list_or
        
        
# 求2个列表A，B的交、并、差

A=[1,3,5,7]
B=[1,3,6,2]
list_e=[]
list_f=[]
list_g=[]

for i in A:
    if i in B:
        list_e.append(i)
print u'交集是：',list_e


for i in A:
    list_f.append(i)
for i in B:
    if i not in list_f:
        list_f.append(i)
print u'并集是',list_f  

      
for i in list_f:
    if i not in list_e:
        list_g.append(i)
print u'差集是：',list_g        
        
      