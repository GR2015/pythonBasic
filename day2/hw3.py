#coding=utf-8
#二分查找
x=[1,2,3,4,5,6,7,85,223]
find=3
max=len(x)
min=0
count=1
while(1):
  idx =(min+max)/2
  if find>x[idx]:
    min=x[idx]
    count+=1
  elif find<x[idx]:
    max=x[idx]
    count+=1
  else:
     print "猜%d次猜对的，%d的索引是%d" %(count,x[idx],idx)
     break