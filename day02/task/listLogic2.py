#!/usr/bin/python
#coding=utf-8
list1 = [False,True,True,False]
list2 = [True,True,False,False]
listAnd = []
listOr = []
for i in range(len(list1)) :
  listAnd.append(list1[i] and list2[i])
  listOr.append(list1[i] or list2[i])
print "********ԭlist*******"
print listAnd
print listOr

print "***** ǰ��������list�ĳ���һ��*****"
print "2��list�Ķ�ӦԪ����and��",listAnd
print "2��list�Ķ�ӦԪ����or��",listOr
    


