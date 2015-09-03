#!/usr/bin/python
#coding=utf-8
'''
队列：先进先出
enqueue - 入队  dequeue - 出队
'''

class Quene(object) :
  def __init__(self, size) :
    self.size = size
    self.quene = []
    
  def __str__(self) :
    return str(self.quene)
    
  def getSize(self) :
    return len(self.quene)
    
  def enqueue(self, items) :
    if self.isfull() :
      return -1
    self.quene.append(items)
  
  def dequeue(self) :
    if self.isempty() :
      return -1
    firstElement = self.quene[0]
    self.quene.remove(firstElement)
    return firstElement
  
  def isfull(self) :
    if len(self.quene) == self.size :
      return True
    return False
  
  def isempty(self) :
    if len(self.quene) == 0 :
      return True
    return False
    
    
if __name__ = '__main__' :
  queneTest = Quene(10)
  for i in range(10) :
    queneTest.enqueue(i)
  
  print queneTest.isfull()

  print queneTest
  print queneTest.getSize()
  
  for i in range(5) :
    print queneTest.dequeue()
  
  print queneTest.isempty()
  print queneTest
  print queneTest.getSize()




