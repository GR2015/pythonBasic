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
print "******* ԭ����*******"
print list1
print list2

print "��list�Ľ�����",set_intersection
print "�����ϵĲ�����",set_union
print "�������ϵĲ��",set_difference





