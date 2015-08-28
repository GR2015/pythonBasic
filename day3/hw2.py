#coding=utf-8
#写一个函数，识别输入字符串是否符合 python 语法的变量名
#包含字母，下划线，和数字
#以字母和下划线开始

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
  

str=raw_input("请输入变量名：")
print isVariable(str)



