#!/usr/bin/python
#coding=utf-8

'''
ʮ����ת������
'''

try :
  num = int(raw_input("please input a decimal :"))
except :
  print "������һ��ʮ����������"
print "ʮ��������",num

list1 = []
if num <= 1 and num >= 0:
  print "������:%d" %(num)
else :
  while num > 1 :
    list1.append(str(num % 2))
    num /= 2
  list1.append(str(num))
  list1.reverse()
  print "������: ",
  octNum = ''.join(list1)
  print octNum
