from graphics import *

win = Window("redSun")
canvas = CanvasFrame(win, 300,300)
center = Point(100,100)
redius = 50
c = Circle(center,redius)
c.draw(canvas)
c.setFill("red")
win.mainloop()