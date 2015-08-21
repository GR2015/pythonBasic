#!/usr/bin/python
#coding=utf-8
'''
输入数字a，n，例如a，4，则打印a+aa+aaa+aaaa之和
'''
try :
  calcNum = int(raw_input("请输入正整数a:"))
  lenN = int(raw_input("请输入正整数n:"))
except :
  print "请输入两个正整数！"
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



