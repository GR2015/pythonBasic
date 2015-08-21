#!/usr/bin/python
#coding=utf-8
'''
将下面数组中的奇数变成它的平方，偶数保持不变。
X = [1,2,3,4,8,7,22,33,88]

'''
X = [1,2,3,4,8,7,22,33,88]
for j,i in enumerate(X) :
  if i % 2 == 1 :
    X[j] = i ** 2
print X
    



