#coding=utf-8 
#���ֲ���

print '****����ָ��������x�б��е�����λ��****' 
x=[1,2,3,4,5,6,7,85,223] 
print 'x�б�=',x 
find=int(raw_input('����������:')) 
s_idx=0   #ָ����ʼ����
e_idx=len(x)  #ָ��ĩβ����
m_idx=len(x)/2  #ָ���м�Ԫ�ص�����
while s_idx<e_idx:  #��ʼ����>ĩβ�����Ļ�����ѭ��  
 if x[m_idx]>find: 
  e_idx=m_idx 
  m_idx=(s_idx+e_idx)/2 
 elif x[m_idx]<find: 
  s_idx=m_idx 
  m_idx=(s_idx+e_idx)/2 
 elif x[m_idx]==find: 
  f_idx=m_idx 
  print 'Ҫ�ҵ����ֵ�����ֵ��:',m_idx 
  break
