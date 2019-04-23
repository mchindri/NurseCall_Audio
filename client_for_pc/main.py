import socket
import pyaudio
import wave
import time
import threading
from AudioThread import AudioThread


GREEN = 7
YELLOW = 8
RED = 25
CALL_BUTTON = 23
SOS_BUTTON = 24


#ipInitialization
SERVER_IP = '192.168.1.102'
MESSAGES_PORT = 50007

#states
S_HOLD = 1
S_STBY = 2
S_CALL = 3


audio = AudioThread(SERVER_IP)

def sendAudio(server):
	CHUNK = 1024
	wf = wave.open('myAudio.wav', 'rb')
	print(wf.getsampwidth())
	print(wf.getnchannels())
	print(wf.getframerate())
	p = pyaudio.PyAudio()

	'''
	# open stream (2)
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
					channels=wf.getnchannels(),
					rate=wf.getframerate(),
					output=True)
	'''

	# read data
	data = wf.readframes(CHUNK)
	while len(data) > 0:
		server.sendall(data)
		data = wf.readframes(CHUNK)
	
	# play stream (3)
	'''
	while len(data) > 0:
		stream.write(data)
		data = wf.readframes(CHUNK)
	'''
	# stop stream (4)
	#stream.stop_stream()
	#stream.close()

	# close PyAudio (5)
	p.terminate()


def readButtons():
	buttons = ''
	#to simulete CALL and SOS
	if False:
		buttons = 'CALL'
	if False:
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

		sendAudio(s)
		'''
		while (True):
		
			buttons = readButtons()
			serverMsg = ""
			try:
				serverMsg = s.recv(1024) #read server
			except socket.timeout:
				pass
			state = refreshState(state, buttons, serverMsg)		
	
			respondToServer(state, s)
			doActions(state)
			
			#
			
			s.sendall(b'Salut\n')
			msg =''
			try:
				msg = s.recv(1024)
			except socket.timeout:
				pass
			print(['Received from server ', str(msg) ])

			time.sleep(1.0)
		'''
			#
	finally:
		s.close()
		print('Socket deleted')

if __name__ == "__main__":
	main()
