#coding=utf-8 
#��ӡ'*'��ɵ�N����

a=int(raw_input('������һ������2������N:')) 
for i in range(1,(a+1)): 
 for j in range(1,a+1): 
  if i==j or j==1 or j==a: 
   print '*', 
  else: 
   print ' ', 
 print
