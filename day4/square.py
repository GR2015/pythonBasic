from graphics import *

win = Window("Square")
canvas = CanvasFrame(win, 300,300)
p1 = Point(50,50)
p2 = Point(60,60)
sq = Rectangle(p1,p2)
sq.draw(canvas)
win.mainloop()
