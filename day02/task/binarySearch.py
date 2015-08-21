#!/usr/bin/python
#coding=utf-8
'''
对列表进行2分查找，要查找的元素从键盘输入。

解题核心：
要实现二分查找的列表必须是有序列表

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




print "原列表为:",list1
try :
  find = int(raw_input("请输入要查找的数："))
except :
  print "请输入正整数！"
  exit()

result = binary_search(find)
if result != -1 : 
  print "要找的元素%d的序号为：%d" %(find,result)
else :
  print "未找到！"




