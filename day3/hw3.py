#coding=utf-8
#д2�������ֱ�ͳ��һ���ַ�������������ĸ�����ֵĸ��� 
def countAlpha(s):
  numAlpha=0
  for i in s:
    if i>="a" and i<="z" or i>="A" and i<="Z":
      numAlpha+=1

  return numAlpha


def countNum(s):
  numDigit=0
  for i in s:
    if i>="0" and i<="9":
      numDigit+=1

  return numDigit


s=raw_input("�������ַ�����")
print "��ĸ����Ϊ��%d�����ָ���Ϊ:%d" %(countAlpha(s),countNum(s))
     
     

