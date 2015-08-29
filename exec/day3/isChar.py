#coding=utf-8
#统计字符串里面所有字母的个数
def ch_count(str):
 cnt=0
 for i in str:
  if (i>='a' and i<='z') or (i>='A' and i<='Z'):   
   cnt+=1
 return cnt

print '字母个数：',ch_count('kdsfjfkdjsf4348348%^&')
