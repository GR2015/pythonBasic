'''a=100
b='200'
try :
  print a+b
except TypeError:
  print "type wrong"'''

def functionName(level):
    if level<1:
        raise Exception('Invalid level!',level)

print functionName(0)



'''try:
  print 1
except "Invalid level!":
  print 2
else:
  print 3'''




