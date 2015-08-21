# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 20:35:46 2015

@author: cindychen
"""
#二分查找
a=[1,3,5,8,12,50]
s=int(raw_input('input a number:'))
low=0
high=len(a)-1
mid=(low+high)/2
flag=0
while high>=low:
    if a[mid]==s:
        flag=1
        print 'a[%d] is %d' %(mid,s)
        break
    elif a[mid]>s:
        high=mid-1
    else:
        low=mid+1
    mid=(low+high)/2
    
if flag==0:
    print 'not found'