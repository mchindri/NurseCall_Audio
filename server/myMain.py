import socket
import time
import traceback

from ClientHandler import *

from myGlobals import *

HOST = ''
MESSAGES_PORT =  50007

def do():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	#init interface

	try:
		s.bind((HOST, MESSAGES_PORT))
		s.listen()
		print('Server started')
		print('Waiting connection')
		conn, addr = s.accept()
		print('Client connected')

		newClient = ClientHandler(conn, addr)

		
		connectedClients.append(newClient)	
	finally:
		pass
		#s.close()

if __name__ == "__main__":
	main()
