#!/usr/bin/python
#coding=utf-8
#强 >=8  并且 密码包含字母和数字
#中 >=8, 或者包含字母，或者数字
#弱 <8 ，包含字母或者数字
digitNum = 0
alphaNum = 0
otherNum = 0
passwd = raw_input("input:")
passwdLen = len(passwd)
if passwdLen >= 8 :
  for i in passwd :
    if i >= 'A' and i <= 'Z' or i >= 'a' and i <= 'z' :
      alphaNum += 1
    elif i >= '0' and i <= '9' :
      digitNum += 1
    else :
      otherNum += 1
  if alphaNum == passwdLen or digitNum == passwdLen :
    print "中"
  else :
    print "强"
else :
  print "弱"
