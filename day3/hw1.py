#coding=utf-8

#һ���ַ��� list��ÿ��Ԫ���� 1 �� ip��������ִ������� ip

def mostIP(lista):
  dip={}
  #IP�͸������浽�ֵ���
  for i in lista:
    if dip.has_key(i):
      dip[i]+=1
    else:
      dip[i]=1
 
  #IP�������浽�б��У�����ȡ���һ�������
  listv=[]
  for k,v in dip.items():
    listv.append(v)

  listv.sort() 
  max=listv[-1]

  #�����ֵ���ֵ����key����IP
  #���ܴ��ڶ��IP���ִ�����ͬ������ʹ��list����
  listk=[]
  for k in dip.keys():
    if dip[k]==max:
      listk.append(k)
   
  return listk


a=["10.1.0.1","10.1.0.2","10.1.0.1","10.1.2.58","10.1.0.2"]
print "a=",a
print "���ִ�������IPΪ:", mostIP(a)