
#coding=utf-8
class enqueue(object):
	def __init__(self,size):  #���캯��
		self.size=size
		self.enqueue=[]
	
	def __str__(self):
		return self.enqueue
		
	def push(self,x):  #������
		if self.isfull():  #����������ˣ�����-1
			return -1
		else:
			self.enqueue.append(x)


	def pop(self):    #������
		if self.isempty():  #�������Ϊ�շ���-1
			return -1
		else:
			return self.enqueue.pop(0)
			
	def isempty(self):  #�ж϶����Ƿ�Ϊ�գ�Ϊ�շ���True
		if self.enqueue==[]:
			return True
		else:
			return False
			
	def isfull(self):  #�ж϶����Ƿ����ˣ����˷���True
		if len(self.enqueue)==self.size:
			return True
		else:
			return False
			
	def getSize(self):  #���ض��г���
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
