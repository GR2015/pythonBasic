#coding=utf-8
#��ӡ'*'��ɵĿ���

a=int(raw_input('������һ������2������N:'))
for i in range(1,(a+1)):
	if i==1 or i==a:
		for j in range(1,a+1):
			print '*',
		print
	else:
		for j in range(1,a+1):
			if j==1 or j==a:
				print '*',
			else:
				print ' ',
		print 		
