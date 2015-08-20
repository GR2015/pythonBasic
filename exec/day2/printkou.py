#coding=utf-8
#打印'*'组成的口字

a=int(raw_input('请输入一个大于2的整数N:'))
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
