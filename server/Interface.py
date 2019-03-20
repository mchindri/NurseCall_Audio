
from tkinter import *
import tkinter.font as tkFont
from threading import Thread
import time
import debug as D
import Synchronizer

class Interface():
	def __init__(self, buttons, alarm):
		D.P("Creating interface")
		self.win = Tk()
		self.myFont = tkFont.Font(family = 'Helvetica', size = 10, weight = 'bold')
		self.win.title("First GUI")
		self.win.attributes('-fullscreen', True)
		#self.win.geometry('800x400')
		self.blinkers = []
		self.buttons = buttons
		self.alarm = alarm
		self.alarm.draw(self.win, self.myFont)
		self.addButtons()
		self.addDefaultButtons()
		self.addClock()
		Synchronizer.init(self.win, self.blinkers, alarm.blinker)
	def __del__(self):
		D.P("Deleting Interface")
		self.win.quit()

	def addClock(self):
		cFont = tkFont.Font(family = 'Helvetica', size = 30, weight = 'bold')
		self.clock =  Label(self.win, font=cFont, text="", bg = None)
		self.clock.pack()
		self.clock.place(x = 300, y = 250, height = 100, width = 200) 
		self.data =  Label(self.win, font=self.myFont, text="", bg = None)
		self.data.pack()
		self.data.place(x = 300, y = 300, height = 40, width = 200) 
		self.updateClock()

	def updateClock(self):
		clock = time.strftime("%H:%M:%S\n")
		data = time.strftime("%A, %d/%m/%Y")
		self.clock.configure(text = clock)
		self.data.configure(text = data)
		self.win.after(1000, self.updateClock)

	def addButtons(self):
		D.P("Adding buttons to interface")
		for i in self.buttons:
			but = Button(self.win, 
				text = i.name,
				font = self.myFont,
				command = i.command,
				bg = i.color,
				activebackground = i.color)
			i.addReferences(self.win, but, self.alarm)
			self.blinkers.append(i.blinker)
			but.pack()
			but.place(x = i.x_poz, y = i.y_poz, height = i.height, width = i.width)		
	def exit(self):
		self.win.quit()
	def start(self):
		D.P("Starting win loop")
		self.win.mainloop()

	def addDefaultButtons(self):
		#exit button
		but = Button(self.win, text="Exit", font=self.myFont, command = self.exit, bg = "Blue", activebackground = "Blue")
		but.pack()
		but.place(x = 10, y = 10, height = 40, width = 40)

		#title
		titlu = Label(self.win, font=self.myFont, text="              NURSE CALL SYSTEM  ----- MIHAIL CHINDRIS AND FLORIN PERI")
		titlu.pack()
		titlu.place(x = 95, y = 10, height = 50, width = 600)
