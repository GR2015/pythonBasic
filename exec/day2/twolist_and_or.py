#coding=utf-8 
#对2个list的对应元素求and，or

a=[True,False,True,False] 
b=[False,True,True,False] 
list_and=[] 
list_or=[] 
for i in range(len(a)):    #列表a或列表b的长度作为循环次数   
 list_and.append(a[i] and b[i]) 
 list_or.append(a[i] or b[i]) 
print '原list1=',a
print '原list2=',b
print 'list_and=',list_and 
print 'list_or=',list_or
