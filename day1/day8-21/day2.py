#!/usr/bin/python
#coding=utf-8
#二分查找

a = [1,2,3,4,33,222]
a.sort()

def binary_search(find) :
  i = 0
  j = len(a)
  try :
    while i <= j :
      mid = (i + j) / 2
      if a[mid] == find :
        return mid
      elif a[mid] > find :
        j = mid -1
      elif a[mid] < find :
        i = mid + 1
  except IndexError :
    return -1
  return -1




print "原列表为:",a
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
