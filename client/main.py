import socket
import pyaudio
import wave
import time
import RPi.GPIO as GPIO
import threading
from AudioThread import AudioThread


GREEN = 7
YELLOW = 8
RED = 25
CALL_BUTTON = 23
SOS_BUTTON = 24

## seting pins
GPIO.setmode(GPIO.BCM) #pins header type
GPIO.setup(CALL_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SOS_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(GREEN, GPIO.OUT) #LED to GPIO24
GPIO.setup(YELLOW, GPIO.OUT) #LED to GPIO24
GPIO.setup(RED, GPIO.OUT) #LED to GPIO24

#ipInitialization
SERVER_IP = '192.168.1.114'
MESSAGES_PORT = 50007

#states
S_HOLD = 1
S_STBY = 2
S_CALL = 3


audio = AudioThread(SERVER_IP)

def setLeds(state):
	if state == S_CALL:
		GPIO.output(RED, True)
		GPIO.output(GREEN,False)
		GPIO.output(YELLOW, True)
	elif state == S_HOLD:
		GPIO.output(RED, True)
		GPIO.output(GREEN, True)
		GPIO.output(YELLOW, False)
	elif state == S_STBY:
		GPIO.output(RED, False)
		GPIO.output(GREEN, True)
		GPIO.output(YELLOW, True)

def readButtons():
	buttons = ''
	if GPIO.input(CALL_BUTTON) == False:
		buttons = 'CALL'
	if GPIO.input(SOS_BUTTON) == False:
		buttons = 'SOS'
	return buttons
	
def refreshState(state, buttons, serverMsg):
	if state == S_STBY and buttons == 'CALL':
		print('Changing to state Hold')
		state = S_HOLD
	elif state == S_HOLD and serverMsg == b'RESPOND':
		print('Changing to state Call')
		state = S_CALL
	elif state == S_CALL and serverMsg == b'STOP':
		print('Changing to state stand-by')
		state = S_STBY
	return state

def respondToServer(state, s):
	if state == S_HOLD:
		s.sendall(b'CALL')
		

def doActions(state):
	if state == S_STBY:
		audio.stop()
		print('Stop thread')
	elif state == S_HOLD:
		audio.prepare()
		print('Init thread')
	elif state == S_CALL:
		audio.start()
		print('Start thread')

def main():
	print('Client started')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	state = S_STBY
	try:	
		print('Connecting to server')
		s.connect((SERVER_IP, MESSAGES_PORT))
		print('Connected succesfully')

		s.settimeout(1.0)	

		while (True):
			buttons = readButtons()
			serverMsg = ""
			try:
				serverMsg = s.recv(1024) #read server
			except socket.timeout as err:
				pass
			state = refreshState(state, buttons, serverMsg)		
	
			respondToServer(state, s)
			setLeds(state)
			doActions(state)
			
			time.sleep(1.0)
	finally:
		s.close()
		GPIO.cleanup()
		print('Socket deleted')

if __name__ == "__main__":
	main()
	GPIO.cleanup()
