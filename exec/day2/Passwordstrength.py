#coding=utf-8
#�������ǿ��

password=raw_input('���������봮')
chr_num=0
digit_num=0
passwdLen=len(password)

for i in password:
	if i in '!@#$%':
		chr_num+=1
	elif i>='0' and i<='9':
		digit_num+=1

if len(password)>=8 and chr_num>0 and digit_num>0:
	print '����ǿ'
if (len(password)>=8 and chr_num>0 and not digit_num>0) or (len(password)>=8 and digit_num>0 and not chr_num>0) or (digit_num>0 and chr_num>0 and not len(password)>=8):
	print '������'
if (len(password)>=8 and not chr_num>0 and not digit_num>0) or  (not len(password)>=8 and digit_num>0 and not chr_num>0) or (not len(password)>=8 and not digit_num>0 and chr_num>0):
	print '������'
