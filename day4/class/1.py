#coding=utf-8

import math

def math2(a,b,c):
  if b*b-4*a*c<0:
    return False
  elif b*b-4*a*c==0:
    x1=-(b/(2*a))
    x2=-(b/(2*a))
    return x1,x2
  else:
    x1=(-b+math.sqrt(b*b-4*a*c))/2*a
    x2=(-b-math.sqrt(b*b-4*a*c))/2*a
    return x1,x2
  
print math2(2,6,3)