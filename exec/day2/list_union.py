#coding=utf-8 
#��2���б�A��B�Ľ���������

a=[1,2,3] 
b=[2,3,4] 
new_listsame=[] 
new_listdiff=[] 


for i in a: 
 if i in b:      
  new_listsame.append(i) 
 else: 
  new_listdiff.append(i) 
for i in b:        
 if i not in a:  
  new_listdiff.append(i) 
  
new_listunion=new_listdiff+new_listsame  

print 'a=',a 
print 'b=',b 
print 'a��b�Ĳ���',new_listunion 
print 'a��b�Ľ�����',new_listsame 
print 'a��b�Ĳ��',new_listdiff
