#coding=UTF-8

#��һ��
for i in range(3):
  print "  |"*2,"\n","_"*9


#�ڶ���
#1
import math
print "(3*5)/(2+3)����",(3*5)/(2+3)
#2
print "7+9��ƽ��������2����",math.sqrt(7+9)*2
#3
print "(4-7)��3�η�����",(4-7)**3
#4
#5
print "angle_test=sin(pi/4)+cos(pi/4)/2����",math.sin(math.pi/4)+math.cos(math.pi/4)/2
#6
print "ceiling_test=[276/19]+2log7(12)����",math.ceil(276/19)+math.log(12,7)*2



#������
a=False
b=True
c=False
print "b and c����",b and c
print "b or c����",b or c
print "not a or b����",not a or b
print "(a and b) or not c����",(a and b) or not c
print "not b and nor (a or c)����",not b and nor (a or c)



#������
#1
a_list=[3,5,6,12]
print a_list[0]#��ȫ���룬��Ӧ����3
#2
print a_list[-1]#��ȫ���룬��Ӧ����12
#3
print a_list[1:]#��ȫ���룬��Ӧ����[5,6,12]
#4
a_list=[3,5,6,12]
for x in a_list: print x, #��ȫ���룬��Ӧ����3 5 6 12
print ""
#5
a_list.reverse()
print a_list#��ȫ���룬��Ӧ����[12 6 5 3]
#6
a_list=[3,5,6,12]
for x in a_list: print 3*x, #Ӧ�����9 15 18 36
print ""
#7
b_list=[]
for x in a_list: 
  x=x>5
  b_list.append(x) 
print b_list #��ȫ���룬��Ӧ����[False False True True]




#������
str_before="ABCDEFGHIGKLMNOPQRSTUVWXYZ"
str_aftermove0=str_before[3:]+str_before[:3]
print str_aftermove0
#��չ1 
#����
str_leftmove1=str_before[-2:]+str_before[:-2]
print str_leftmove1
#����
str_rightmove2=str_before[2:]+str_before[:2]
print str_rightmove2
#��չ2
str=raw_input("�������ַ�����")
movenumber=int(raw_input("�������ƶ�λ�����������ƣ��������ƣ���"))
def move(str,movenumber):
  print str,movenumber
  str_aftermove=str[movenumber:]+str[:movenumber]
  print str_aftermove
move(str,movenumber)



  
  
