#coding=utf-8 
#求2个列表A，B的交、并、差

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
print 'a和b的并集',new_listunion 
print 'a和b的交集：',new_listsame 
print 'a和b的差集：',new_listdiff
