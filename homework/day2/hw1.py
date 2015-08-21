# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 19:35:21 2015

@author: cindychen
"""

# 打印出‘N’图案
n=6
for i in range(n):
    for j in range(n):
        if j==0:
            print '*',
        elif j==i:
            print '*',
        elif j==n-1:
            print '*',
        else:
            print ' ',
    print 
    
print 

# 打印出‘口’图案
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1:
            print '*',
        elif j==0 or j==n-1:
            print '*',
        else:
            print ' ',
    print 
    
            