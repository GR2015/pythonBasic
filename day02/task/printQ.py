#!/usr/bin/python
#coding=utf-8
try :
  lenQ = int(raw_input("������Ҫ��ӡ�������εı߳���"))
  for i in range(lenQ) :
    for j in range(lenQ) :
      if i == 0 or i == (lenQ - 1) or j == 0 or j == (lenQ - 1) :
        print "*",
      else :
        print " ",
    print 
except ValueError :
  print "������һ����������"






