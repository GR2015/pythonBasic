#!/usr/bin/python
#coding=utf-8

'''
十进制转二进制
'''

try :
  num = int(raw_input("please input a decimal :"))
except :
  print "请输入一个十进制整数！"
print "十进制数：",num

list1 = []
if num <= 1 and num >= 0:
  print "二进制:%d" %(num)
else :
  while num > 1 :
    list1.append(str(num % 2))
    num /= 2
  list1.append(str(num))
  list1.reverse()
  print "二进制: ",
  octNum = ''.join(list1)
  print octNum
