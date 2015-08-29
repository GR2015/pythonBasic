
#coding=utf-8
#统计字符串里面所有数字的个数
def digit_count(str):
 cnt=0
 for i in str:
  if i>='0' and i<='9': #判断i是否是数字，如果是的话cnt+1
   cnt+=1
 return cnt
print '字符串中数字的个数：',digit_count('kdsfjfkdjsf4348348%^&')