import relayCommand
from tkinter import *
from Blinker import *

class Alarm:
	ON = 1
	OFF = 0
	def __init__(self):
		D.P("Initialized alarm")
		self.relayId = 15
		self.name = "Stop\nAlarm"
		self.width = 100
		self.height = 70
		self.x_poz = 350
		self.y_poz = 355
		self.color = "green"
		self.displayRef = None
		self.status = self.OFF

	def set(self):
		D.P("Activating alarm")
		if self.status == self.OFF:
			self.status = self.ON
			relayCommand.setRelay(self.relayId)
			self.blinker.start()
		
	def unSet(self):
		D.P("Desactivating alarm")
		self.status = self.OFF
		relayCommand.unsetRelay(self.relayId)
		self.blinker.stop()

	def isSet(self):
		if self.status == self.ON:
			return True
		return False

	def refresh(self):
		#stop blinker
		self.unSet()

	def draw(self, win, myFont):
		self.displayRef = Button(win, text = self.name, font = myFont, command = self.refresh, bg = self.color, activebackground = self.color)
		self.displayRef.pack()
		self.displayRef.place(x = self.x_poz, y = self.y_poz, height = self.height, width = self.width)
		self.blinker = Blinker(win, self.displayRef, self.color)
