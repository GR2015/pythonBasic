from graphics import *


win = Window("car")
canvas = CanvasFrame(win, 300,300)

p1 = Point(50,50)
p2 = Point(150,100)
sq = Rectangle(p1,p2)
sq.draw(canvas)

center = Point(75,113)
redius = 13
clo = Circle(center,redius)
clo.draw(canvas)
clo.setFill("black")

center = Point(75,113)
redius = 10
cli = Circle(center,redius)
cli.draw(canvas)
cli.setFill("white")


cro=clo.clone()
cro.draw(canvas)
cri=cli.clone()
cri.draw(canvas)
cro.move(45,0)
cri.move(45,0)

'''len=canvas.width-p2.x
carlen=p2.x-p1.x
step=1
for i in range(20):
  sq.move(step,0)
  cro.move(step,0)
  cri.move(step,0)
  clo.move(step,0)
  cli.move(step,0)'''



#sq.move(13,0)
win.mainloop()
