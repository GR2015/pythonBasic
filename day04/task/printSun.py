#!/usr/bin/python
#coding=utf-8

from graphics import *

def printCircle():
  win = Window("Circle")   #设置窗口的Title
  canvas = CanvasFrame(win, 300, 300)    #使用画布画一个300 * 300的窗口
  p0 = Point(150, 150)     #创建一个坐标原点的实例
  
  c = Circle(p0, 50)    #创建Circle类的实例对象c
  

  c.draw(canvas)   #调用c对象的draw方法开始画圆
  c.setOutline('yellow')  #填充圆的外线颜色为黄色
  c.setFill('red')    #填充圆内的颜色为红色
  
  #canvas.getMouse()    # 鼠标点击窗口后退出
  win.mainloop()     #让窗口一直存在，不一闪而过
printCircle()