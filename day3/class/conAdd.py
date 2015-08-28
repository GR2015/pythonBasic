#coding=utf-8
#用递归的方式求列表的和
def f(n):
  idx=len(l)
  if n-1<0:
    return l[-1]
  elif n>idx:
    n=idx
    return f(idx)    
  else:
    return f(n-1)+l[n-1]

l=[2,3,4,1,3,4,3,6,4]
for i in range(len(l)):
  print "f(%d)=%d" %(i,f(i))

