#coding=utf-8
from graphics import *
win=Window('Tetris')
canvas=CanvasFrame(win,1000,1000)

#��Բ��
center=Point(50,270) #Բ��,����Point���Բ��
radius=30   #�뾶
circle=Circle(center,radius)  ##��һ�����ӵ�Բ�ģ�ͨ��Point���Բ��
circle.draw(canvas)  #����draw������Բ
circle.setFill('red')  #����setFill��Բ�����ɫ

#��������
p1=Point(120,245)  #����Point������������Ͻǵĵ������
p2=Point(170,295)  #����Point������������½ǵĵ������
rectangle=Rectangle(p1,p2) #����rectangleʵ��
rectangle.draw(canvas)  #����Rectangle������������
rectangle.setFill('blue')  #����setFill�������������ɫ

#��С��
#��ɫ����
p1=Point(10,10)  #����Point��ó��������Ͻǵĵ������
p2=Point(340,139)  #����Point��ó��������½ǵĵ������
rectangle=Rectangle(p1,p2)  #����rectangleʵ��
rectangle.draw(canvas)  #����Rectangle������������
rectangle.setFill('red')  #����setFill�������������ɫ


#������
center_1=Point(80,172)  #��һ�����ӵ�Բ�ģ�ͨ��Point���Բ��
center_2=Point(270,172)  #�ڶ������ӵ�Բ�ģ�ͨ��Point���Բ��
radius=33  #���ӵİ뾶
radius_in=10 #��������С���ӵİ뾶

#�������ӵ�ʵ��
circle_1=Circle(center_1,radius)  #��һ�����ֵ�ʵ��
circle_1_in=Circle(center_1,radius_in) #��һ�����������С���ӵ�ʵ��
circle_2=Circle(center_2,radius)  #�ڶ������ֵ�ʵ��
circle_2_in=Circle(center_2,radius_in) #�ڶ������������С���ӵ�ʵ��

#����draw����������
circle_1.draw(canvas)  #����һ������
circle_1_in.draw(canvas) #����һ�����������С����
circle_2.draw(canvas)  #���ڶ�������
circle_2_in.draw(canvas) #���ڶ������������С����

#����setFill���������������ɫ
circle_1.setFill('yellow')  #����һ�����������ɫ
circle_2.setFill('yellow')  #��һ�����������С���������ɫ
circle_1_in.setFill('pink')  #�ڶ������������ɫ
circle_2_in.setFill('pink')  #�ڶ������������С���������ɫ

win.mainloop()