
#coding=utf-8
#ͳ���ַ��������������ֵĸ���
def digit_count(str):
 cnt=0
 for i in str:
  if i>='0' and i<='9': #�ж�i�Ƿ������֣�����ǵĻ�cnt+1
   cnt+=1
 return cnt
print '�ַ��������ֵĸ�����',digit_count('kdsfjfkdjsf4348348%^&')