#coding=utf-8
#��2���б�A��B�Ľ���������

a=[1,2,3]
b=[2,3,4]
c=[]
#��
print "a=",a
print "b=",b
print "��"

for i in a:
  if i in b:
    c.append(i)

print c



#��
print "��"
d=[]
for i in a:
  if i not in b:
    d.append(i)

d.extend(b)
print d

#��
print "��"
e=[]
f=[]
for i in a:
  if i not in b:
      e.append(i)

print "a-b=",e

for j in b:
  if j not in a:
    f.append(j)

print "b-a=",f
