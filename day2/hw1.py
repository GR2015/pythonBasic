#coding=utf-8
#��ӡ��ͼ��
print "��ӡ��ͼ��n=2"
n=2
for i in range(n):
  print '**',
  print "" 


print "��ӡ��ͼ��n=4"
n=4
for i in range(n):
  for j in range(n):
    if j==0 or i==0:
      print "*",  
    elif j==n-1 or i==n-1:
      print "*",
    else:
      print " ",
  print "\n"


print "��ӡNͼ��"
n=3
for i in range(n):
  for j in range(n):
    if j==0 or j==n-1 or i==j:
      print "*",  
    else:
      print " ",
  print "\n"

#****��ӡ4*4������
print "��ӡ4*4������"
n=4
for i in range(n):
  for j in range(n):
    print '*',
  print ""    



#****��ӡ������
print "��ӡ������"
n=4
for i in range(n):
  for j in range(i+1):
    print '*',
  print ""  


   


#��ӡXͼ��
print "��ӡXͼ��n=3"
n=3
for i in range(n):
  for j in range(n):
    if i==j:
      print "*",
    elif i+j==n-1:
      print "*",
    else:
      print " ",
  print "\n"


print "��ӡXͼ��n=4"
n=4
for i in range(n):
  for j in range(n):
    if i==j:
      print "*",
    elif i+j==n-1:
      print "*",
    else:
      print " ",
  print "\n"







     