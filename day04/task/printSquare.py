#!/usr/bin/python
#coding=utf-8

from graphics import *

#画矩形
def printRectangle(canvas, pt1, pt2, cr):
  
  rt = Rectangle(pt1, pt2)
  rt.draw(canvas)
  rt.setOutline('yellow') 
  rt.setFill(cr)


def printSquare() :
  win = Window("Car")
  canvas = CanvasFrame(win, 300, 300)
  
  pt1 = Point(50, 50)
  pt2 = Point(150, 150)
  #画矩形
  printRectangle(canvas, pt1, pt2, 'blue')
  
  win.mainloop() 
  
printSquare()


  
