#!/usr/bin/python
#coding=utf-8

print "***************�ַ�����λ����***************"
str_input = raw_input("input a string :")
try :
  length = int(raw_input("��������λ�ĳ��ȣ����������ƣ����������ƣ�:"))
except :
  print "please input a interger !"
if length >= 0 :
  str_input = str_input[-length : ] + str_input[ : -length]
elif length < 0 :
  str_input = str_input[ : -length] + str_input[-length : ]
print "��λ����ַ�����",str_input

