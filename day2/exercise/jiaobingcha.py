#coding=utf-8
#求2个列表A，B的交、并、差

a=[1,2,3]
b=[2,3,4]
c=[]
#交
print "a=",a
print "b=",b
print "交"

for i in a:
  if i in b:
    c.append(i)

print c



#并
print "并"
d=[]
for i in a:
  if i not in b:
    d.append(i)

d.extend(b)
print d

#差
print "差"
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
