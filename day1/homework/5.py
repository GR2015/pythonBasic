#coding=utf-8

s="abcdefghijklmnopqrstuvwxyz"
print s
print "字符串左移3位：",s[3:]+s[:3]


#扩展1：原串分别左移2位和右移2位怎么做？ 
print "字符串左移2位：",s[2:]+s[:2]

print "字符串右移2位：",s[len(s)-2:]+s[:len(s)-2]

'''扩展2：从键盘接受一个字符串和移位的长度（可以是负数），对一个字符串进行移位，如输入 ‘abcde’ 1 表示右移1位（负数表示左移），结果为’bcdea’
'''
a=raw_input("请输入字符串:")
b=int(raw_input("请输入移动位数（正数表示右移，负数表示左移）:"))
le=len(a)
if b>=0:
  print "右移 %d 位" %b
  print a[le-b:]+a[:le-b]
else:
  b=abs(b)
  print "左移 %d 位" %b
  print a[b:]+a[:b]