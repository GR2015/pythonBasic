#coding=utf-8
'''
ͳ���ַ�������ĸ�����֡������ַ��ֱ�ĸ���
'''

digitNum = 0
alphaNum = 0
otherNum = 0

s = raw_input("please input a string��")

for i in s :
  if i.isdigit() :
    digitNum += 1
  elif i.isalpha() :
    alphaNum += 1
  else :
    otherNum += 1
print "�����У�",digitNum,"��"
print "\n��ĸ�У�",alphaNum,"��"
print "\n�����ַ��У�",otherNum,"��"

'''
��������

for i in s :
  if i >= 'A' and i <= 'Z' or i >= 'a' and i <= 'z' :
    alphaNum += 1
  elif i >= '0' and i <= '9' :
    digitNum += 1
  else :
    otherNum += 1
print "�����У�",digitNum,"��"
print "\n��ĸ�У�",alphaNum,"��"
print "\n�����ַ��У�",otherNum,"��"
'''
