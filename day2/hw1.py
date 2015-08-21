#coding=utf-8
#打印口图形
print "打印口图形n=2"
n=2
for i in range(n):
  print '**',
  print "" 


print "打印口图形n=4"
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


print "打印N图形"
n=3
for i in range(n):
  for j in range(n):
    if j==0 or j==n-1 or i==j:
      print "*",  
    else:
      print " ",
  print "\n"

#****打印4*4正方形
print "打印4*4正方形"
n=4
for i in range(n):
  for j in range(n):
    print '*',
  print ""    



#****打印三角形
print "打印三角形"
n=4
for i in range(n):
  for j in range(i+1):
    print '*',
  print ""  


   


#打印X图形
print "打印X图形n=3"
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


print "打印X图形n=4"
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







     