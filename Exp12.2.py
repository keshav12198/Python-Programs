from graphics import *
import datetime
import time
class DigitalClock:
	def __init__(self,hour,minute,second):
		self.hour = hour
		self.minute = minute
		self.second = second
	def draw(self,win):
		rect = Rectangle(Point(40,15),Point(165,80))
		rect.setFill('grey')
		rect.draw(win)
		message = Text(Point(100,50),str(self.hour)+':'+str(self.minute)+':'+str(self.second))
		message.setStyle('italic')
		message.setSize(20)
		message.draw(win)
		time.sleep(1)
		message.undraw()
		

win = GraphWin("DigitalClock",300,300)
now = datetime.datetime.now()
clock = DigitalClock(now.hour,now.minute,now.second)
while True:
	clock.draw(win)
	now = datetime.datetime.now()
	clock.second=now.second
	clock.hour=now.hour
	clock.minute=now.minute
	

win.mainloop()
