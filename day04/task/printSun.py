#!/usr/bin/python
#coding=utf-8

from graphics import *

def printCircle():
  win = Window("Circle")   #���ô��ڵ�Title
  canvas = CanvasFrame(win, 300, 300)    #ʹ�û�����һ��300 * 300�Ĵ���
  p0 = Point(150, 150)     #����һ������ԭ���ʵ��
  
  c = Circle(p0, 50)    #����Circle���ʵ������c
  

  c.draw(canvas)   #����c�����draw������ʼ��Բ
  c.setOutline('yellow')  #���Բ��������ɫΪ��ɫ
  c.setFill('red')    #���Բ�ڵ���ɫΪ��ɫ
  
  #canvas.getMouse()    # ��������ں��˳�
  win.mainloop()     #�ô���һֱ���ڣ���һ������
printCircle()