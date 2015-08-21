#!/usr/bin/python
#coding=utf-8
'''
解题思路：
首先判断n中是否包含第一个特殊数字，如果包含就报Fizz
  否则判断是否是三个数的倍数，如果是报FizzBuzzWhizz
    否则判断是否是某两个数的倍数，如果是报对应两个单词
      否则判断是否是某一个数的倍数，如果是报对应的单词
        否则报对应的数字。'''

listUnit = [-1,-1,-1]
listWord = ['Fizz','Buzz','Whizz']

#判断是否是任意两个数的倍数，是则返回对应的单词组合，否则返回字符串'NO'
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
  
#判断是任意一个数的倍数，是则返回对应的单词，否则返回'NO'
def checkOneNum(num) :
  for i in range(len(listUnit)) :
    if num % listUnit[i] == 0 :
      return listWord[i]
  return 'NO'
  
#按照游戏规则，检查所报数实际应该报什么
def checkNum(num) :
  decadeNum = num / 10  #报数数的十位
  unitNum = num % 10   #报数数的个位
  twoStr = checkTwoNum(num)
  oneStr = checkOneNum(num)
  if decadeNum == listUnit[0] or unitNum == listUnit[0]:
    #是否包含第一个特殊数
    return "Fizz"
  elif num % listUnit[0] == 0 and num % listUnit[1] == 0 and listUnit[2] == 0 :
    #是否仅是三个数的倍数  
    return "FizzBuzzWhizz"
  elif twoStr != 'NO' :
    #是否仅是任意两个数的倍数
    return twoStr
  elif oneStr != 'NO' :
    #是否仅是某一个数的倍数
    return oneStr
  return num
    
#***************************程序入口*****************************
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
print "******************100名学生开始报数*******************"
for n in range(1, 101) :
  if n % 10 == 1 and (n != 100):
    print "\n"
  print checkNum(n),
  
  














