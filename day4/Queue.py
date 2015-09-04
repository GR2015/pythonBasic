#coding=utf-8
#队列类实现
class Queue(object):
  
  def __init__(self,size):
    self.size=size
    self.queue=[]

  def enqueue(self,item):
    if self.isfull():
      print "队列已满"
    else:
      self.queue.append(item)

  def dequeue(self):
    if self.isempty():
      print "队列是空的"
    else:
      del self.queue[0]

      

  def getSize(self):
    return len(self.queue)

  def isfull(self):
    if len(self.queue)==self.size:
      return True
    else:
      return False

  def isempty(self):
    if len(self.queue)==0:
      return True
    else:
      return False

  def __str__(self):
    return str(self.queue)

queue1=Queue(10)
print queue1.getSize()
print queue1.isempty()
print queue1.dequeue()


for i in range(10):
  queue1.enqueue(i)


print queue1
print queue1.getSize()
print queue1.isfull()
print queue1.enqueue(10)

print queue1.dequeue()
print queue1.getSize()
print queue1






  
  