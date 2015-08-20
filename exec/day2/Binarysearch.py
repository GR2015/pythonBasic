#coding=utf-8 
#二分查找

print '****查找指定数字在x列表中的索引位置****' 
x=[1,2,3,4,5,6,7,85,223] 
print 'x列表=',x 
find=int(raw_input('请输入数字:')) 
s_idx=0   #指定起始索引
e_idx=len(x)  #指定末尾索引
m_idx=len(x)/2  #指定中间元素的索引
while s_idx<e_idx:  #起始索引>末尾索引的话结束循环  
 if x[m_idx]>find: 
  e_idx=m_idx 
  m_idx=(s_idx+e_idx)/2 
 elif x[m_idx]<find: 
  s_idx=m_idx 
  m_idx=(s_idx+e_idx)/2 
 elif x[m_idx]==find: 
  f_idx=m_idx 
  print '要找的数字的索引值是:',m_idx 
  break
