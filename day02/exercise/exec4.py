#!/usr/bin/python
#coding=utf-8
'''
1.��ӡ2000-3000֮�䱻7����������5�����������ԣ��ָ���
2.��ӡ1/2, 1/3, 1/4, .....,1/10
'''
print "***** ��ӡ2000-3000֮�䱻7����������5�����������ԣ��ָ� *****"

for i in range(2000,3001) :
 if i % 7 == 0 and i % 5 != 0 :
   print "%d," %(i),

print "\n\n********** ��ӡ1/2, 1/3, 1/4, .....,1/10 **********"
i = 2
while i <= 10 :
  print "1/%d," %(i),
  i += 1




