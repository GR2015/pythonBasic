#coding=utf-8
#从键盘接受一个字符串和移位的长度（可以是负数），对一个字符串进行移位，如输入 ‘abcde’ 1 表示左移1位（负数表示左移），结果为’bcdea’

move_list=[]

a_list=raw_input('请输入一串字符串：')
a=int(raw_input('请输入移动的位数，正数往左移动，负数往右移动'))


move_list=a_list[a:]+a_list[:a]
	
print move_list
