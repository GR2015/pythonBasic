# coding=utf-8
a = [True, False, False, True, False]
resultAnd = a[0]
resultOr = a[0]
listNot = []
print a
for i in a:
    resultAnd = resultAnd and i
    resultOr = resultOr or i
    listNot.append(not i)
print "a中所有元素and结果：", resultAnd
print "a中所有元素or结果：", resultOr
print "a中所有元素not结果：", listNot
