#coding=utf-8
#ͳ���ַ�������������ĸ�ĸ���
def ch_count(str):
 cnt=0
 for i in str:
  if (i>='a' and i<='z') or (i>='A' and i<='Z'):   
   cnt+=1
 return cnt

print '��ĸ������',ch_count('kdsfjfkdjsf4348348%^&')
