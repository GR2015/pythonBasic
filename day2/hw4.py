#coding=utf-8
'''
�������
passwd='dsfaf12'

����ǿ�ȵ�һ�⣺
ǿ >=8  ���� ���������ĸ������
�� >=8, ���߰�����ĸ����������
�� <8 ��������ĸ��������

c1 : ����>=8
c2: ������ĸ
c3: ��������

ǿ������c1,c2,c3
�У�����c1 and (c2 or c3)
��������c2 or c3


����ǿ�ȵڶ��⣺
c1 : ����>=8
c2: ��������
c3: ������@#��%

ǿ������c1,c2,c3
��: ����2������
��������1������
'''

#����ǿ�ȵ�һ��
passwd='dsfaf12'
#passwd=raw_input("���������룺")
x=len(passwd)
if x>=8:
  flagc1=True
else:
  flagc1=False

for i in passwd:
  if i >='a' and i <='z' or i >='A' and i <='Z':
    flagc2=True
    break
  else:
    flagc2=False

for i in passwd:
  if i >='0' and i <='9':
    flagc3=True
    break
  else:
    flagc3=False

while (flagc1):
  if (flagc2 and flagc3):
    print "����ǿ��Ϊ��ǿ"
    break
  elif (flagc2 or flagc3):
    print "����ǿ��Ϊ����"
    break
  else:
    print "�����������ĸ�����ַ�"
    break

while (flagc1==False):
  if (flagc2 or flagc3):
    print "����ǿ��Ϊ����"
    break
  else:
    print "�����������ĸ�����ַ�"
    break
  

#����ǿ�ȵڶ��⣺
passwd='dsfaf12'
#passwd=raw_input("���������룺")
x=len(passwd)
if x>=8:
  flagc1=True
  c1=1
else:
  flagc1=False
  c1=0

for i in passwd:
  if i in "��@#��%":
    flagc2=True
    c2=1
    break
  else:
    flagc2=False
    c2=0

for i in passwd:
  if i >='0' and i <='9':
    flagc3=True
    c3=1
    break
  else:
    flagc3=False
    c3=0

c=c1+c2+c3
if c==3:
  print "ǿ"
elif c==2:
  print "��"
elif c==1:
  print "��"
else:
  print "̫��"