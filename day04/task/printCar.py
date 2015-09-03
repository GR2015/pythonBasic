#!/usr/bin/python
#coding=utf-8

from graphics import *

#������
def printRectangle(canvas, pt1, pt2, cr):
  
  rt = Rectangle(pt1, pt2)
  rt.draw(canvas)
  rt.setOutline('yellow') 
  rt.setFill(cr)

#��Բ
def printCircle(canvas, pCenter, radius, cr):

  circle = Circle(pCenter, radius)  #����Circle���ʵ������c
  circle.draw(canvas)               #����c�����draw������ʼ��Բ
  #circle.setOutline(color)        #���Բ��������ɫΪ��ɫ
  #cr = 'gray'
  circle.setFill(cr) 
  
def printCar() :
  win = Window("Car")
  canvas = CanvasFrame(win, 1000, 500)
  
  #*******������*****
  #��������
  pt1 = Point(0, 0)
  pt2 = Point(160, 60)
  #������
  printRectangle(canvas, pt1, pt2, 'yellow')
  
  #��Բ
  #�����ְ뾶
  radiusOuter = 25  #��Բ�뾶
  radiusInner = 10  #��Բ�뾶
  
  pOuterCirLeft = Point(40, 85)  #�����Բ������
  pCenterRight = Point(120, 85)  #ǰ����Բ������
  
  printCircle(canvas, pOuterCirLeft, radiusOuter, 'yellow') #�����Բ 
  printCircle(canvas, pOuterCirLeft, radiusInner, 'pink')   #�����Բ
  
  printCircle(canvas, pCenterRight, radiusOuter, 'yellow')  #ǰ����Բ
  printCircle(canvas, pCenterRight, radiusInner, 'pink')    #ǰ����Բ
  
  #canvas.getMouse() #һ����������ڣ��Ի������˳�
  win.mainloop()
  
printCar()
