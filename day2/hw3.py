#coding=utf-8
#���ֲ���
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
     print "��%d�β¶Եģ�%d��������%d" %(count,x[idx],idx)
     break