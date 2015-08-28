#coding=utf-8
def add(x,*y):
  a=x
  for i in y:
    a+=i
  print a
  #return a
  
def sub(x,*y):
  s=x
  for i in y:
     s-=i
  print s  
  return s
  
def multi(x,*y):
  m=x
  for i in y:
     m*=i
  print m
  return m
  
def div(x,*y):
  d=x
  for i in y:
    if i==0:
      print "除数不能为0"
      break
    else:
      d=d/i
      print d
      return d

  
add(1,2,3,4,5)
sub(1,2,3,4,5)
multi(1,2,3,4,5)
div(60,2,3,4,5)
div(1,0,2,3,4,5)






