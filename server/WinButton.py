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
			if G.callPressed[G.ROOM1] == False:
				G.callPressed[G.ROOM1] = True
				G.lastCallPressed[G.ROOM1] = True
				
			print ('Pressed Room 1')
		if self.id == 6:
			if G.callPressed[G.ROOM2] == False:
				G.callPressed[G.ROOM2] = True
				G.lastCallPressed[G.ROOM2] = True
			print ('Pressed Room 2')
		if self.id == 14:
			if G.callPressed[G.ROOM3] == False:
				G.callPressed[G.ROOM3] = True
				G.lastCallPressed[G.ROOM3] = True
			print ('Pressed Room 3')
		D.P("Refresh button " + str(self.name))
		relayCommand.unsetRelay(self.relayId)
		self.blinker.stop()
		self.input.unSet()
