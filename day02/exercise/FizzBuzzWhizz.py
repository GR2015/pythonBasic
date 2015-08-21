#!/usr/bin/python
#coding=utf-8
'''
����˼·��
�����ж�n���Ƿ������һ���������֣���������ͱ�Fizz
  �����ж��Ƿ����������ı���������Ǳ�FizzBuzzWhizz
    �����ж��Ƿ���ĳ�������ı���������Ǳ���Ӧ��������
      �����ж��Ƿ���ĳһ�����ı���������Ǳ���Ӧ�ĵ���
        ���򱨶�Ӧ�����֡�'''

listUnit = [-1,-1,-1]
listWord = ['Fizz','Buzz','Whizz']

#�ж��Ƿ��������������ı��������򷵻ض�Ӧ�ĵ�����ϣ����򷵻��ַ���'NO'
def checkTwoNum(num) :
  returnStr = ''
  n = 0
  for i in range(len(listUnit)) :
    if num % listUnit[i] == 0 :
      returnStr += listWord[i]
      n += 1
  if n == 2 :
    return returnStr
  return 'NO'
  
#�ж�������һ�����ı��������򷵻ض�Ӧ�ĵ��ʣ����򷵻�'NO'
def checkOneNum(num) :
  for i in range(len(listUnit)) :
    if num % listUnit[i] == 0 :
      return listWord[i]
  return 'NO'
  
#������Ϸ���򣬼��������ʵ��Ӧ�ñ�ʲô
def checkNum(num) :
  decadeNum = num / 10  #��������ʮλ
  unitNum = num % 10   #�������ĸ�λ
  twoStr = checkTwoNum(num)
  oneStr = checkOneNum(num)
  if decadeNum == listUnit[0] or unitNum == listUnit[0]:
    #�Ƿ������һ��������
    return "Fizz"
  elif num % listUnit[0] == 0 and num % listUnit[1] == 0 and listUnit[2] == 0 :
    #�Ƿ�����������ı���  
    return "FizzBuzzWhizz"
  elif twoStr != 'NO' :
    #�Ƿ���������������ı���
    return twoStr
  elif oneStr != 'NO' :
    #�Ƿ����ĳһ�����ı���
    return oneStr
  return num
    
#***************************�������*****************************
try : 
  n = 0
  while n < 3 :
    print "please input the %d positive integer :" %(n + 1)
    listUnit[n] = int(raw_input())
    if listUnit[n] <= 0 or listUnit[n] >= 10 :
      print "please input a positive integer n(0 < n <= 9) :"
      continue
    elif listUnit.count(listUnit[n]) > 1 :
      print "Please enter 3 different positive integers!"
      continue
    else :
      n += 1
except :
  print "please input three integers"
print "******************100��ѧ����ʼ����*******************"
for n in range(1, 101) :
  if n % 10 == 1 and (n != 100):
    print "\n"
  print checkNum(n),
  
  














