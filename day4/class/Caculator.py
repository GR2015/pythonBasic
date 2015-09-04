#coding=utf-8

class Caculator(object):

  def __init__(self,x,y):
    self.x=x
    self.y=y

  def add(self):
    return self.x+self.y
  
  def sub(self):
    return self.x-self.y
  
  def multi(self):
    return self.x*self.y
  
  def div(self):
    if self.y==0:
      print "除数不能为0"
    else:
      return self.x/self.y


s=Caculator(5,2)
print s.add()
print s.sub()
print s.multi()
print s.div()