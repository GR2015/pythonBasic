#!/usr/bin/python
#coding=utf-8
try :
  lenQ = int(raw_input("请输入要打印的正方形的边长："))
  for i in range(lenQ) :
    for j in range(lenQ) :
      if i == 0 or i == (lenQ - 1) or j == 0 or j == (lenQ - 1) :
        print "*",
      else :
        print " ",
    print 
except ValueError :
  print "请输入一个正整数！"






