#coding=utf-8
'''
统计字符串中字母、数字、其他字符分别的个数
'''

digitNum = 0
alphaNum = 0
otherNum = 0

s = raw_input("please input a string：")

for i in s :
  if i.isdigit() :
    digitNum += 1
  elif i.isalpha() :
    alphaNum += 1
  else :
    otherNum += 1
print "数字有：",digitNum,"个"
print "\n字母有：",alphaNum,"个"
print "\n其他字符有：",otherNum,"个"

'''
方法二：

for i in s :
  if i >= 'A' and i <= 'Z' or i >= 'a' and i <= 'z' :
    alphaNum += 1
  elif i >= '0' and i <= '9' :
    digitNum += 1
  else :
    otherNum += 1
print "数字有：",digitNum,"个"
print "\n字母有：",alphaNum,"个"
print "\n其他字符有：",otherNum,"个"
'''
