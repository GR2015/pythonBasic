#coding=utf-8
#��һ��list������Ԫ����and��or��not
#��2��list�Ķ�ӦԪ����and��or�����ɽ��list

# һ��list������Ԫ����and
a=[True,False,True]
c=True

for i in a:
  c=c and i
  print c,
print""

# һ��list������Ԫ����or
a=[True,False,True]
d=False

for i in a:
  d=d or i
  print d,
print""


# һ��list������Ԫ����not
a=[True,False,True]
e=True

for i in a:
  e=not i
  print e,
print""

#2��list�Ķ�ӦԪ����and
a=[True,False,True]
b=[True,True,True]
f=[]
for i in range(len(a)):
  f.append(a[i] and b[i])

print "a and b=",f


#2��list�Ķ�ӦԪ����or
a=[True,False,True]
b=[True,True,True]
g=[]
for i in range(len(a)):
  g.append(a[i] or b[i])

print "a or b=",g

  