#!/usr/bin/python
#coding=utf-8

from graphics import *

#画矩形
def printRectangle(canvas, pt1, pt2, cr):
  
  rt = Rectangle(pt1, pt2)
  rt.draw(canvas)
  rt.setOutline('yellow') 
  rt.setFill(cr)

#画圆
def printCircle(canvas, pCenter, radius, cr):

  circle = Circle(pCenter, radius)  #创建Circle类的实例对象c
  circle.draw(canvas)               #调用c对象的draw方法开始画圆
  #circle.setOutline(color)        #填充圆的外线颜色为黄色
  #cr = 'gray'
  circle.setFill(cr) 
  
def printCar() :
  win = Window("Car")
  canvas = CanvasFrame(win, 1000, 500)
  
  #*******画车身*****
  #矩形坐标
  pt1 = Point(0, 0)
  pt2 = Point(160, 60)
  #画矩形
  printRectangle(canvas, pt1, pt2, 'yellow')
  
  #外圆
  #车滚轮半径
  radiusOuter = 25  #外圆半径
  radiusInner = 10  #内圆半径
  
  pOuterCirLeft = Point(40, 85)  #后滚轮圆心坐标
  pCenterRight = Point(120, 85)  #前滚轮圆心坐标
  
  printCircle(canvas, pOuterCirLeft, radiusOuter, 'yellow') #后滚外圆 
  printCircle(canvas, pOuterCirLeft, radiusInner, 'pink')   #后滚内圆
  
  printCircle(canvas, pCenterRight, radiusOuter, 'yellow')  #前滚外圆
  printCircle(canvas, pCenterRight, radiusInner, 'pink')    #前滚内圆
  
  #canvas.getMouse() #一旦鼠标点击窗口，对话窗口退出
  win.mainloop()
  
printCar()
