#coding=utf-8 
#��һ��list������Ԫ����and or not

a=[True,False,True,False] 
flag_not=[] 
flag_and=True          
flag_or=False          
for i in a:      
 flag_and=flag_and and i 
 flag_or=flag_or or i 
 flag_not.append(not i) 
print 'ԭlist=',a 
print 'flag_and=',flag_and 
print 'flag_or=',flag_or 
print 'flag_not=',flag_not
