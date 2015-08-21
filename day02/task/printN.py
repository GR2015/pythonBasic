#!/usr/bin/python
#coding=utf-8
lenN = int(raw_input("请输入要打印图案N的边长："))
for i in range(lenN) :
  for j in range(lenN) :
    if j == 0 or j == (lenN - 1) :
      print "*",
    elif i == j :
      print "*",
    else :
      print " ",
  print 



