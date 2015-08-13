#coding=utf-8

#字符串移位（提示：利用分片） 原字符串: ABCDEFGHIJKLMNOPQRSTUVWXYZ 移位后的字符串: DEFGHIJKLMNOPQRSTUVWXYZABC
a_list='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_list=a_list[3:]+a_list[:3]
print 'new_list=',new_list

#'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 左移2位和右移2位
a_list='ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
left_move2_list=a_list[2:]+a_list[:2]
print 'left_move2_list=',left_move2_list

#'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 右移2位
right_move2_list=a_list[-2:]+a_list[:-2]
print 'right_move2_list=',right_move2_list
