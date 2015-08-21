# coding=utf-8
# 求2个列表A，B的交、并、差
a = [1, 2, 'q', 3]
b = [2, 3, 'w']
c = []
d = []
x = []
for i in a:
    x.append(i)
    if i in b:
        c.append(i)
    else:
        d.append(i)
for i in b:
    if i not in x:
        x.append(i)
    if i not in a:
        d.append(i)



print 'a=', a
print  'b=', b
print  'a和b的并集', x
print 'a和b的交集', c
print 'a和b的差集', d
