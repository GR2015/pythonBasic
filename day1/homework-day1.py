#coding=UTF-8

#第一题
for i in range(3):
  print "  |"*2,"\n","_"*9


#第二题
#1
import math
print "(3*5)/(2+3)等于",(3*5)/(2+3)
#2
print "7+9的平方根，乘2等于",math.sqrt(7+9)*2
#3
print "(4-7)的3次方等于",(4-7)**3
#4
#5
print "angle_test=sin(pi/4)+cos(pi/4)/2等于",math.sin(math.pi/4)+math.cos(math.pi/4)/2
#6
print "ceiling_test=[276/19]+2log7(12)等于",math.ceil(276/19)+math.log(12,7)*2



#第三题
a=False
b=True
c=False
print "b and c返回",b and c
print "b or c返回",b or c
print "not a or b返回",not a or b
print "(a and b) or not c返回",(a and b) or not c
print "not b and nor (a or c)返回",not b and nor (a or c)



#第四题
#1
a_list=[3,5,6,12]
print a_list[0]#补全代码，答案应该是3
#2
print a_list[-1]#补全代码，答案应该是12
#3
print a_list[1:]#补全代码，答案应该是[5,6,12]
#4
a_list=[3,5,6,12]
for x in a_list: print x, #补全代码，答案应该是3 5 6 12
print ""
#5
a_list.reverse()
print a_list#补全代码，答案应该是[12 6 5 3]
#6
a_list=[3,5,6,12]
for x in a_list: print 3*x, #应该输出9 15 18 36
print ""
#7
b_list=[]
for x in a_list: 
  x=x>5
  b_list.append(x) 
print b_list #补全代码，答案应该是[False False True True]




#第五题
str_before="ABCDEFGHIGKLMNOPQRSTUVWXYZ"
str_aftermove0=str_before[3:]+str_before[:3]
print str_aftermove0
#扩展1 
#左移
str_leftmove1=str_before[-2:]+str_before[:-2]
print str_leftmove1
#右移
str_rightmove2=str_before[2:]+str_before[:2]
print str_rightmove2
#扩展2
str=raw_input("请输入字符串：")
movenumber=int(raw_input("请输入移动位数（负数左移，正数右移）："))
def move(str,movenumber):
  print str,movenumber
  str_aftermove=str[movenumber:]+str[:movenumber]
  print str_aftermove
move(str,movenumber)



  
  
