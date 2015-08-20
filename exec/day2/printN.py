#coding=utf-8 
#打印'*'组成的N字形

a=int(raw_input('请输入一个大于2的整数N:')) 
for i in range(1,(a+1)): 
 for j in range(1,a+1): 
  if i==j or j==1 or j==a: 
   print '*', 
  else: 
   print ' ', 
 print
