#coding=utf-8

class Caculator(object):

  def __init__(self):
    #self.x=x
    #self.y=y
    n=1

  
  def add(self,x,y):
    return x+y
  
  def sub(self,x,y):
    return x-y
  
  def multi(self,x,y):
    return x*y
  
  def div(self,x,y):
    if y==0:
      print "除数不能为0"
    else:
      return x/y


s=Caculator()
print s.add(5,2)
print s.sub(5,2)
print s.multi(5,2)
print s.div(5,2)