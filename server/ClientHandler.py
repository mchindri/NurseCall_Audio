import socket
import time
from threading import Thread
from AudioThread import AudioThread

import myGlobals as G


S_STBY = 1
S_WAIT = 2
S_CALL = 3


class ClientHandler(Thread):
	
	def __init__(self, conn, addr):
		Thread.__init__(self)
		self.conn = conn

		self.conn.settimeout(1.0)

		self.ip, self.port = addr
		self.audio = AudioThread(self.ip)

		self.active = True
		self.intf_msg = ''
		self.client_msg = ''
		self.start()
	def refreshState(self, state):
		if state == S_STBY and self.client_msg == b'CALL':
			G.event.on_change(5)
			state = S_WAIT
		elif state == S_WAIT and self.intf_msg == 'RESPOND':
			state = S_CALL
		elif state == S_CALL and self.intf_msg == 'STOP':
			state = S_STBY
		return state

	def respondToClient(self, state):
		if state == S_STBY:
			self.conn.sendall(b'STOP')
		elif state == S_WAIT:
			self.conn.sendall(b'HOLD')
		elif state == S_CALL:
			self.conn.sendall(b'RESPOND')

	def doActions(self, state):
		if state == S_STBY:
			self.audio.stop()
			print('Stop thread')
		elif state == S_WAIT:
			self.audio.prepare()
			print('Init thread')
		elif state == S_CALL:
			self.audio.start()
			print('Start thread')

	def run(self):
		state = S_STBY
		try:
			while self.active:
				#interf = readInterface() #il actualizeaza interfata
				self.client_msg = ""
				try:
					self.client_msg = self.conn.recv(1024)
				except socket.timeout as err:
					pass
				global callPressed
				global alarmPressed
				if G.callPressed == True:
					self.intf_msg = 'RESPOND'
					G.callPressed = False

				if G.alarmPressed == True:
					self.intf_msg = 'STOP'
					G.alarmPressed = False			
				
	
				state = self.refreshState(state)
				self.respondToClient(state)
				self.doActions(state)

				print('Client handler running')
				time.sleep(1.0)
		finally:
			self.conn.close()
	def end(self):
		self.active = False
