#!/usr/bin/python
#coding=utf-8
#ǿ >=8  ���� ���������ĸ������
#�� >=8, ���߰�����ĸ����������
#�� <8 ��������ĸ��������
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
    print "��"
  else :
    print "ǿ"
else :
  print "��"
