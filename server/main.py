import socket
import time
import traceback

from ClientHandler import *

from myGlobals import *

HOST = ''
MESSAGES_PORT =  50007

def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	#init interface

	try:
		s.bind((HOST, MESSAGES_PORT))
		s.listen()
		print('Server started')
		while(True):
			print('Waiting connection')
			conn, addr = s.accept()
			print('Client connected')

			newClient = ClientHandler(conn, addr)

			i = 0
			while True:
				if i == 10:
					newClient.intf_msg = "RESPOND"

				if i == 20:
					newClient.intf_msg = "STOP"
					i = 0
				i = i + 1	
				time.sleep(1.0)

			connectedClients.append(newClient)	
	finally:
		s.close()

if __name__ == "__main__":
	main()
