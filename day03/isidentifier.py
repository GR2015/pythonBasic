#!/usr/bin/python
#coding=utf-8
'''
写一个函数，识别输入的字符串是否符合python语法标识符
判断标识符标准：
1.由可由字母、数字、下划线组成
2.不能以数字开头
3.标识符中间不能有空白字符
4.字母不区分大小写
invalid syntax

'''

def isidentifier(str1) :
  strVar = str1
  if not strVar.isspace() and len(strVar) != 0:
    strVar = strVar.strip()
    if strVar.count(' ') == 0 and strVar.count('\t') == 0 and \
       strVar.count('\r') == 0 and strVar.count('\n') == 0:
      for i in range(len(strVar)) :
        if i == 0 :
          #print strVar[i]
          if strVar[i].isalpha() or strVar[i] == '_' :
            continue
          else :
            return False
        if strVar[i].isalnum() or strVar[i] == '_' :
          continue
        else :
          return False
      return True
    else :
      return False 
  return False
    
str1 = raw_input("please input a string :")
if isidentifier(str1) :
  print "Valid identifier!"
else :
  print "invalid identifier!"
  



