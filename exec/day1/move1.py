#coding=utf-8

#�ַ�����λ����ʾ�����÷�Ƭ�� ԭ�ַ���: ABCDEFGHIJKLMNOPQRSTUVWXYZ ��λ����ַ���: DEFGHIJKLMNOPQRSTUVWXYZABC
a_list='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_list=a_list[3:]+a_list[:3]
print 'new_list=',new_list

#'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ����2λ������2λ
a_list='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
left_move2_list=a_list[2:]+a_list[:2]
print 'left_move2_list=',left_move2_list

#'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ����2λ
right_move2_list=a_list[-2:]+a_list[:-2]
print 'right_move2_list=',right_move2_list
