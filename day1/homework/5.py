#coding=utf-8

s="abcdefghijklmnopqrstuvwxyz"
print s
print "�ַ�������3λ��",s[3:]+s[:3]


#��չ1��ԭ���ֱ�����2λ������2λ��ô���� 
print "�ַ�������2λ��",s[2:]+s[:2]

print "�ַ�������2λ��",s[len(s)-2:]+s[:len(s)-2]

'''��չ2���Ӽ��̽���һ���ַ�������λ�ĳ��ȣ������Ǹ���������һ���ַ���������λ�������� ��abcde�� 1 ��ʾ����1λ��������ʾ���ƣ������Ϊ��bcdea��
'''
a=raw_input("�������ַ���:")
b=int(raw_input("�������ƶ�λ����������ʾ���ƣ�������ʾ���ƣ�:"))
le=len(a)
if b>=0:
  print "���� %d λ" %b
  print a[le-b:]+a[:le-b]
else:
  b=abs(b)
  print "���� %d λ" %b
  print a[b:]+a[:b]