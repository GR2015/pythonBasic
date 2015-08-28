#coding=utf-8
#写2个函数分别统计一个字符串里面所有字母，数字的个数 
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


s="abcd1234ef56q"
print "字母个数为：%d，数字个数为:%d" %(countAlpha(s),countNum(s))
     
     

