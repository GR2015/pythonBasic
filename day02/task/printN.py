#!/usr/bin/python
#coding=utf-8
lenN = int(raw_input("������Ҫ��ӡͼ��N�ı߳���"))
for i in range(lenN) :
  for j in range(lenN) :
    if j == 0 or j == (lenN - 1) :
      print "*",
    elif i == j :
      print "*",
    else :
      print " ",
  print 



