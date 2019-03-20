import debug as D

class Blinker(object):
	ON = 1
	OFF = 0
	TIME = 250
	ON_COLOR = "red"
	def __init__(self, win, bref, color):
		self.bref = bref
		self.win = win
		self.color = color
		self.status = self.OFF
		self.active = False
	
	def start(self):
		self.active = True

	def stop(self):
		self.active = False
		self.bref.configure(bg = self.color, activebackground = self.color)

	def run(self, status):
		if self.active == True:
			if status == 1:
				self.bref.configure(bg = self.color, activebackground = self.color)
				self.status = self.OFF
			else:
				self.bref.configure(bg = self.ON_COLOR, activebackground = self.ON_COLOR)
				self.status = self.ON
		else:
			self.stop()
		
