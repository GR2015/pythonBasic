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
print "list中所有元素and结果：",resultAnd
print "list中所有元素or结果：",resultOr
print "list中所有元素not结果：",listNot





