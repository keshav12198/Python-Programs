from wheel import *
from graphics import *
class Car:
	def __init__(self,w1,w2,r1):
		self.w1=w1
		self.w2=w2
		self.r1=r1
	def draw(self,win):
		self.r1.setFill('red')
		self.r1.setOutline('black')
		self.r1.setWidth(2)
		self.w1.c.setFill('black')
		self.w2.c.setFill('black')
		self.r1.draw(win)
		self.w1.c.draw(win)
		self.w2.c.draw(win)

r1 = Rectangle(Point(100,100),Point(200,150))
w1 = Wheel(Point(100,150),25)
w2 = Wheel(Point(200,150),25)
c = Car(w1,w2,r1)
win = GraphWin("Car",400,400)
c.draw(win)
win.mainloop()

