#coding=utf-8
#f(0)=0,f(1)=1,f(n)=f(n-1)+f(n-2)

'''def f(n):
  
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
   result=f(n-1)+f(n-2)
   return result
    
print f(50)'''

d={}
for i in range(0,50):
    d[i] = -1

d[0] = 0
d[1] = 1

def f(n):
    if(n<=0):
        return 0
    elif (n==1):
        return 1
    else:
        #m = f(n-1) + f(n-2)
        if d[n-1] != -1:  #如果d[n-1]没有赋值，重新执行
            m1 = d[n-1]
        else:
            m1 = f(n-1)
        if d[n-2] != -1:
            m2 = d[n-2]
        else:
            m2 = f(n-2)
        m = m1+m2
        d[n] = m
        return m 


