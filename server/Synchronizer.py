import debug as D

TIME = 250
win = None
buttons = []
alarm = None
status = 0

def init(winRef, myButtons, myAlarm):
	global win
	win = winRef
	global buttons
	buttons = myButtons
	global alarm
	alarm = myAlarm
	run()



def run():
	D.P("Draw rutine running")
	global win
	global status
	global buttons
	global alarm
	for i in buttons:
		i.run(status)
	if status == 1:
		status = 0
	else:
		status = 1
	alarm.run(status)
	win.after(TIME, run)
