
#coding=utf-8
class enqueue(object):
	def __init__(self,size):  #构造函数
		self.size=size
		self.enqueue=[]
	
	def __str__(self):
		return self.enqueue
		
	def push(self,x):  #进队列
		if self.isfull():  #如果队列满了，返回-1
			return -1
		else:
			self.enqueue.append(x)


	def pop(self):    #出队列
		if self.isempty():  #如果队列为空返回-1
			return -1
		else:
			return self.enqueue.pop(0)
			
	def isempty(self):  #判断队列是否为空，为空返回True
		if self.enqueue==[]:
			return True
		else:
			return False
			
	def isfull(self):  #判断队列是否满了，满了返回True
		if len(self.enqueue)==self.size:
			return True
		else:
			return False
			
	def getSize(self):  #返回队列长度
		num=len(self.enqueue)
		return num

		
enqueueTest=enqueue(5)

print 'the size of stack is:',enqueueTest.getSize()
print 'isempty:',enqueueTest.isempty()
print 'isfull:',enqueueTest.isfull()
print 'stack=',enqueueTest.__str__()

for i in range(5):
	enqueueTest.push(i)
	
print 'the size of stack is:',enqueueTest.getSize()
print 'isempty:',enqueueTest.isempty()
print 'isfull:',enqueueTest.isfull()
print 'stack=',enqueueTest.__str__()



for i in range(5):
	print 'print the element of popenqueue:',
	print enqueueTest.pop()

print 'the size of stack is:',enqueueTest.getSize()
print 'isempty:',enqueueTest.isempty()
print 'isfull:',enqueueTest.isfull()
print 'stack=',enqueueTest.__str__()
