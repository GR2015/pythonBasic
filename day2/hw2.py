#coding=utf-8
#对一个list的所有元素求and，or，not
#对2个list的对应元素求and，or，生成结果list

# 一个list的所有元素求and
a=[True,False,True]
c=True

for i in a:
  c=c and i
  print c,
print""

# 一个list的所有元素求or
a=[True,False,True]
d=False

for i in a:
  d=d or i
  print d,
print""


# 一个list的所有元素求not
a=[True,False,True]
e=True

for i in a:
  e=not i
  print e,
print""

#2个list的对应元素求and
a=[True,False,True]
b=[True,True,True]
f=[]
for i in range(len(a)):
  f.append(a[i] and b[i])

print "a and b=",f


#2个list的对应元素求or
a=[True,False,True]
b=[True,True,True]
g=[]
for i in range(len(a)):
  g.append(a[i] or b[i])

print "a or b=",g

  