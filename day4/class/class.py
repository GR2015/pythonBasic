#coding=utf-8
#定义类
class Employee(object):
  empCount=0
  
  def __init__(self,name,salary): #构造函数，self一定有，只本身，name,salary是参数
    self.name=name
    self.salary=salary
    Employee.empCount+=1
    
  def displayCount(self):
    print "Total Emplyee %d" %Employee.empCount

  def displayEmployee(self):
    print "Name:",self.name,",Salary:",self.salary

#创建实例
emp1 = Employee('tom',21)
emp2 = Employee('test',50)

#调用方法
emp1.displayEmployee()

#调用属性
print emp1.name
print "Total Emplyee %d" %Employee.empCount
