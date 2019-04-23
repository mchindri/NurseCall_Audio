import socket
import time
from threading import Thread
import pyaudio
import wave
import time
import traceback

AUDIO_PORT = 50010

CHUNK = 8192
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = 'server_output.wav'
WIDTH = 2

S_INIT = 1
S_START = 2
S_STOP = 3

class AudioThread():

	def __init__(self, ip):
		self.ip = ip
		self.state = S_STOP
		self.server = None
		self.client = None

	def prepare(self):
		if self.state == S_INIT:
			return
		self.state = S_INIT
		self.server = ServerThread()

	def start(self):
		if self.state == S_START:
			return
		self.state = S_START
		time.sleep(2.0)
		self.client = ClientThread(self.ip)

	def stop(self):
		if self.state == S_STOP:
			return
		self.state = S_STOP
		self.client.end()
		self.server.end()




class ServerThread(Thread):
	
	def __init__(self):
		Thread.__init__(self)
		self.p = None
		self.stream = None
		self.s = None
		try:	
			self.p = pyaudio.PyAudio()
			self.stream = self.p.open(format=self.p.get_format_from_width(WIDTH),
					channels = CHANNELS,
					rate = RATE,
					output = True,
					frames_per_buffer=CHUNK)
			
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			#init interface
			self.s.bind(('', AUDIO_PORT))
			self.s.listen(1)
			self.active = True
			self.start()
		except Exception:
			traceback.print_exc()
			if self.stream:
				self.stream.stop_stream()
				self.stream.close()
			if self.p:
				self.p.terminate()
			if self.s:
				self.s.close()

	def run(self):

		print('Server waiting for audio client')
		self.conn, self.addr = self.s.accept()
		print('Audio client connected ... Starting Audio')	
		while self.active:
			try:
				#print('RecivingAudio')
				data = self.conn.recv(CHUNK)
				#print(['Recived: ', str(data)])
				self.stream.write(data)		
			except:
				traceback.print_exc()


	def end(self):
		self.active = False
		time.sleep(0.1)
		if self.stream:
			self.stream.stop_stream()
			self.stream.close()
		if self.p:
			self.p.terminate()
		if self.s:
			self.s.close()
		




class ClientThread(Thread):

	def __init__(self, ip):
		Thread.__init__(self)
		self.ip = ip
		self.p = None
		self.stream = None
		self.s = None
		try:
			
			self.p = pyaudio.PyAudio()
			self.stream = self.p.open(format = FORMAT,
				channels = CHANNELS,
				rate = RATE,
				input = True,
				frames_per_buffer = CHUNK)
			
			self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			#init interface
			self.s.connect((self.ip, AUDIO_PORT))	
			print(['connecting to ', self.ip])	
			self.active = True
			self.start()
		except Exception:
			traceback.print_exc()
			if self.stream:
				self.stream.stop_stream()
				self.stream.close()
			if self.p:
				self.p.terminate()
			if self.s:
				self.s.close()

	def run(self):
		while self.active:
			try:
				data = self.stream.read(CHUNK, exception_on_overflow = False)
				#print('SendingAudio')
				#data = b"usless data"
				self.s.sendall(data)			
			except:
				traceback.print_exc()

	def end(self):
		self.active = False
		time.sleep(0.1)
		if self.stream:
			self.stream.stop_stream()
			self.stream.close()
		if self.p:
			self.p.terminate()
		if self.s:
			self.s.close()

