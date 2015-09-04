
def f(a,n,x):
  s0=a+"0"
  s=""
  for i in range(1,n+1):
      s+=a+str(n)+'*'+x+'^'+str(n)+'+'
      n-=1

  return s+s0

a="a"
n=5
x="x"

print f(a,5,x)


'''#from songxia
def f(a,n,x):	
	sum=''
	#N=n+1
	for i in range(n+1):
		if n==0:
			sum+=a+str(n)+'*'+x+'^'+str(n)
		else:
			sum+=a+str(n)+'*'+x+'^'+str(n)+'+'
		n-=1
		
		
	return sum
		
n=3
x=4
print f('a',n,'x')'''
