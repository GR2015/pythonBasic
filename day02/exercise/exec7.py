#!/usr/bin/python
#coding=utf-8
'''
��������a��n������a��4�����ӡa+aa+aaa+aaaa֮��
'''
try :
  calcNum = int(raw_input("������������a:"))
  lenN = int(raw_input("������������n:"))
except :
  print "������������������"
  exit()
sum = 0
result = 0
for i in range(lenN) :
  if i == 0 :
    result = calcNum
  else :
    result += calcNum * (10 ** i)
  if i <= (lenN - 2) :
    print "%d +" %(result),
  else :
    print result,
  sum += result

print "=",sum



