#coding=utf-8
#дһ��������ʶ�������ַ����Ƿ���� python �﷨�ı�����
#������ĸ���»��ߣ�������
#����ĸ���»��߿�ʼ

def isVariable(s):
  if s[0]>="a" and s[0]<="z" or s[0]>="A" and s[0]<="Z" or s[0]=="_":
    for i in s:
      if i>="0" and i<="9":
        flag=True
      elif i>="a" and i<="z" or i>="A" and i<="Z":
        flag=True
      elif i=="_":
        flag=True
      else:
        flag=False
        break
      
      
  else:
    flag=False
    
  return flag
  

str=raw_input("�������������")
print isVariable(str)



