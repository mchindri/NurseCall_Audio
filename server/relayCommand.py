import serial
import debug as D 

#serPort = serial.Serial('/dev/ttyUSB0', 19200, timeout=1)
#serPort = serial.Serial('/dev/ttyACM0', 19200, timeout=1)

def getId(id):
	if (int(id) < 10):
		cid = str(id)
	else:
		cid = chr(55 + int(id))
	return cid

def setRelay(id):
	D.P("Setting relay " + str(id) + " ON")
	msg = "relay on " + getId(id) + "\n\r"
	#serPort.write(msg)
	D.P("Serial sent: " + msg)
def unsetRelay(id):
	D.P("Setting relay " + str(id) + " OFF")
	msg = "relay off " + getId(id) + "\n\r"
	#serPort.write(msg)
	D.P("Serial sent: " + msg)

def closeAll():
	for id in range(0, 16):
		D.P("Closing relay " + str(id))
		unsetRelay(id)

def close():
	closeAll()
	D.P("Closing serial port")
	#serPort.close()
