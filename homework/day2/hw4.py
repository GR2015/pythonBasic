# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:19:47 2015

@author: cindychen
"""

#密码强度
s=raw_input('input passwd:')
a=len(s)
if a>=8:
    A=True
else:
    A=False
    
    
for i in s:
    if i in '0123456789':
        B=True
        break
else:
    B=False
    

for i in s:
    if i in '!@#¥%':
        C=True
        break
else:
    C=False
print A,B,C  
if A and B and C:
    print u'密码强度为强'
elif (A and B) or (A and C) or (B and C):
    print u'密码强度为中'
elif A or B or C:
    print u'密码强度为低' 
else:
    print u'密码不符合要求'
    



   
    