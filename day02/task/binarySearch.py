#!/usr/bin/python
#coding=utf-8
'''
���б����2�ֲ��ң�Ҫ���ҵ�Ԫ�شӼ������롣

������ģ�
Ҫʵ�ֶ��ֲ��ҵ��б�����������б�

'''

list1 = [1,2,3,7,8,9,10,5]
list1.sort()

def binary_search(find) :
  i = 0
  j = len(list1)
  try :
    while i <= j :
      mid = (i + j) / 2
      if list1[mid] == find :
        return mid
      elif list1[mid] > find :
        j = mid -1
      elif list1[mid] < find :
        i = mid + 1
  except IndexError :
    return -1
  return -1




print "ԭ�б�Ϊ:",list1
try :
  find = int(raw_input("������Ҫ���ҵ�����"))
except :
  print "��������������"
  exit()

result = binary_search(find)
if result != -1 : 
  print "Ҫ�ҵ�Ԫ��%d�����Ϊ��%d" %(find,result)
else :
  print "δ�ҵ���"




