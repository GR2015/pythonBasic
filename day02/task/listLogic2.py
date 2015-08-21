#!/usr/bin/python
#coding=utf-8
list1 = [False,True,True,False]
list2 = [True,True,False,False]
listAnd = []
listOr = []
for i in range(len(list1)) :
  listAnd.append(list1[i] and list2[i])
  listOr.append(list1[i] or list2[i])
print "********原list*******"
print listAnd
print listOr

print "***** 前提是两个list的长度一致*****"
print "2个list的对应元素求and：",listAnd
print "2个list的对应元素求or：",listOr
    


