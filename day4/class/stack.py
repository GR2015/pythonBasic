#coding=utf-8

class Stack(object):

  def __init__(self,size):
    self.size=size
    self.stack=[]


  def push(self,item):
    if self.isfull():
      print "Õ»ÒÑÂú"
    else:
      self.stack.append(item)

 
  def pop(self):
    if self.isempty():
      print "Õ»ÊÇ¿ÕµÄ£¡"
    else:
      self.stack.pop()

       

  def getSize(self):
    return len(self.stack)
    

  def isempty(self):
     if len(self.stack)==0:
       return True
     else:
       return False

  def isfull(self):
    if len(self.stack)==self.size:
       return True
    else:
       return False      

  def __str__(self):
    return str(self.stack)


#print Stack(100)

stack1=Stack(10)
stack1.pop()
for i in range(10):
  stack1.push(i)


print stack1.getSize()
print stack1.isempty()
print stack1.isfull()
print stack1
stack1.push('a')

stack1.pop()
print stack1.getSize()
print stack1.isempty()
print stack1.isfull()
print stack1
  