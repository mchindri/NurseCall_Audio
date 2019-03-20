from InputButton import *
from Blinker import *
import debug as d
import relayCommand
import Alarm

import myGlobals as G

class WinButton(object):
	def __init__(self, id, relayId, name, width, height, x_poz, y_poz, color):
		self.winRef = None
		self.id = id
		self.relayId = relayId
		self.name = name
		self.command = self.refresh
		self.width = width
		self.height = height
		self.x_poz = x_poz
		self.y_poz = y_poz
		self.color = color
		self.input = InputButton(self.id, self.activationCallback)

	def addReferences(self, win, winRef, alarm):
		self.winRef = winRef
		self.blinker = Blinker(win, self.winRef, self.color)
		self.alarm = alarm

	def activationCallback(self):
		D.P("Button pressed")
		if self.input.isSet() == False:
			relayCommand.setRelay(self.relayId)
			self.input.set()
			self.blinker.start()
		self.alarm.set()
	
	def refresh(self):
		if self.id == 5:
			if G.callPressed == False:
				G.callPressed = True
			print ('Pressed Room 5')
		D.P("Refresh button " + str(self.name))
		relayCommand.unsetRelay(self.relayId)
		self.blinker.stop()
		self.input.unSet()
