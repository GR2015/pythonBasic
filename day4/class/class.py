#coding=utf-8
#������
class Employee(object):
  empCount=0
  
  def __init__(self,name,salary): #���캯����selfһ���У�ֻ����name,salary�ǲ���
    self.name=name
    self.salary=salary
    Employee.empCount+=1
    
  def displayCount(self):
    print "Total Emplyee %d" %Employee.empCount

  def displayEmployee(self):
    print "Name:",self.name,",Salary:",self.salary

#����ʵ��
emp1 = Employee('tom',21)
emp2 = Employee('test',50)

#���÷���
emp1.displayEmployee()

#��������
print emp1.name
print "Total Emplyee %d" %Employee.empCount
