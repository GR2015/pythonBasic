#coding=utf-8
#�Ӽ��̽���һ���ַ�������λ�ĳ��ȣ������Ǹ���������һ���ַ���������λ�������� ��abcde�� 1 ��ʾ����1λ��������ʾ���ƣ������Ϊ��bcdea��

move_list=[]

a_list=raw_input('������һ���ַ�����')
a=int(raw_input('�������ƶ���λ�������������ƶ������������ƶ�'))


move_list=a_list[a:]+a_list[:a]
	
print move_list
