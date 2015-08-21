#!/usr/bin/python
#coding=utf-8
list1 = [1,2,'g',6,'s',9,'as']
list2 = [3,6,'as','h','g']
set_intersection = []
set_union = []
set_difference = []
for i in list1 :
  if i in list2 :
    set_intersection.append(i)
  elif i not in list2 :
    set_difference.append(i)
set_union = list1 + list2
print "******* 原集合*******"
print list1
print list2

print "两list的交集：",set_intersection
print "两集合的并集：",set_union
print "两个集合的差集：",set_difference





