#!/usr/bin/python
#coding=utf-8

print "***************字符串移位操作***************"
str_input = raw_input("input a string :")
try :
  length = int(raw_input("请输入移位的长度（正数表右移，负数表左移）:"))
except :
  print "please input a interger !"
str_input = str_input[-length : ] + str_input[ : -length]
print "移位后的字符串：",str_input

