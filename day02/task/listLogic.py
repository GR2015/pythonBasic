#!/usr/bin/python
#coding=utf-8
listSour = [True,False,False,True,False]
resultAnd = listSour[0]
resultOr = listSour[0]
listNot = []
print listSour
for i in listSour :
  resultAnd = resultAnd and i
  resultOr = resultOr or i
  listNot.append(not i)
print "list������Ԫ��and�����",resultAnd
print "list������Ԫ��or�����",resultOr
print "list������Ԫ��not�����",listNot





