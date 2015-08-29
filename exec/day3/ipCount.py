#coding=utf-8
##统计列表中每一个IP出现的次数
def count_Num(list1):
 dict1={}  
 for idx,i in enumerate(list1):  
  if not dict1.has_key(i):  
   dict1[i]=1
  else:              
   dict1[i]+=1
 return dict1	  
#找出出现次数最多的IP
def max_Count(dict1):
 max_Num=0  
 for k,v in dict1.items():  
  if max_Num < v:  
   max_Num=v   
   idx=k       
 return idx,max_Num  
     
dict1=count_Num(['10.10.1.10','10.10.2.10','10.10.0.10','10.10.0.10'])
IP,max=max_Count(dict1)
print '%s出现的次数最多，共' %IP,
print '%d次' %max
