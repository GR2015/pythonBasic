#coding=utf-8 
#��2��list�Ķ�ӦԪ����and��or

a=[True,False,True,False] 
b=[False,True,True,False] 
list_and=[] 
list_or=[] 
for i in range(len(a)):    #�б�a���б�b�ĳ�����Ϊѭ������   
 list_and.append(a[i] and b[i]) 
 list_or.append(a[i] or b[i]) 
print 'ԭlist1=',a
print 'ԭlist2=',b
print 'list_and=',list_and 
print 'list_or=',list_or
