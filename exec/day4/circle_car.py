#coding=utf-8
from graphics import *
win=Window('Tetris')
canvas=CanvasFrame(win,1000,1000)

#画圆形
center=Point(50,270) #圆心,调用Point求得圆心
radius=30   #半径
circle=Circle(center,radius)  ##第一个轮子的圆心，通过Point求得圆心
circle.draw(canvas)  #调用draw方法画圆
circle.setFill('red')  #调用setFill给圆填充颜色

#画正方形
p1=Point(120,245)  #调用Point求得正方形左上角的点的坐标
p2=Point(170,295)  #调用Point求得正方形右下角的点的坐标
rectangle=Rectangle(p1,p2) #创建rectangle实例
rectangle.draw(canvas)  #调用Rectangle方法画正方形
rectangle.setFill('blue')  #调用setFill给正方形填充颜色

#画小车
#红色车身
p1=Point(10,10)  #调用Point求得长方形左上角的点的坐标
p2=Point(340,139)  #调用Point求得长方形右下角的点的坐标
rectangle=Rectangle(p1,p2)  #创建rectangle实例
rectangle.draw(canvas)  #调用Rectangle方法画长方形
rectangle.setFill('red')  #调用setFill给长方形填充颜色


#车轮子
center_1=Point(80,172)  #第一个轮子的圆心，通过Point求得圆心
center_2=Point(270,172)  #第二个轮子的圆心，通过Point求得圆心
radius=33  #轮子的半径
radius_in=10 #轮子里面小轮子的半径

#创建轮子的实例
circle_1=Circle(center_1,radius)  #第一个车轮的实例
circle_1_in=Circle(center_1,radius_in) #第一个轮子里面的小轮子的实例
circle_2=Circle(center_2,radius)  #第二个车轮的实例
circle_2_in=Circle(center_2,radius_in) #第二个轮子里面的小轮子的实例

#调用draw方法画轮子
circle_1.draw(canvas)  #画第一个轮子
circle_1_in.draw(canvas) #画第一个轮子里面的小轮子
circle_2.draw(canvas)  #画第二个轮子
circle_2_in.draw(canvas) #画第二个轮子里面的小轮子

#调用setFill方法给轮子填充颜色
circle_1.setFill('yellow')  #给第一个轮子填充颜色
circle_2.setFill('yellow')  #第一个轮子里面的小轮子填充颜色
circle_1_in.setFill('pink')  #第二个轮子填充颜色
circle_2_in.setFill('pink')  #第二个轮子里面的小轮子填充颜色

win.mainloop()