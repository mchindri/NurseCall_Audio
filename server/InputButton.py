#import keyboard
import RPi.GPIO as GPIO
import debug as D
import threading


from myGlobals import *

class InputButton(object):
	"""description of class"""
	OFF = 0
	ON = 1
	GPIO.setmode(GPIO.BCM)

	def __init__(self, id, activationCallback):
		self.activationCallback = activationCallback
		self.buttonID = id
		self.inputPin = id
		self.status = self.OFF
		GPIO.setup(self.inputPin, GPIO.IN)
		self.addEvent()

	def isSet(self):
		if self.status == self.OFF:
			return False
		else:
			return True

	def set(self):
		self.status = self.ON

	def unSet(self):
		self.status = self.OFF

	def activateSwitch(self, pinReaded):
		D.P("Button" + str(self.buttonID) + " activated")
		self.activationCallback()

	def addEvent(self):
		D.P("Setting callback for button " + str(self.buttonID))	
		if self.buttonID == 5:
			event[ROOM1].on_change += self.activateSwitch
		if self.buttonID == 6:
			event[ROOM2].on_change += self.activateSwitch
		if self.buttonID == 14:
			event[ROOM3].on_change += self.activateSwitch
		GPIO.add_event_detect(self.buttonID, GPIO.RISING,
								callback = self.activateSwitch) 

'''
	#for GPIO
	def read(self):
		if self.status == self.OFF:
			if GPIO.input(self.inputPin) == True:
				D.P("Button " + str(self.inputPin) + " pressed")
				self.activateSwitch()
'''
'''
	def read(self):
		#print(str(self.buttonID) + " button readed")
		if keyboard.is_pressed(str(self.buttonID)):
			self.activateSwitch()
			while keyboard.is_pressed(str(self.buttonID)):
            	pass
'''
