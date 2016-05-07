__author__="Paul"
import socket

class TcpClient():
	def Main(self):
		print("TcpClient")
		host = "127.0.0.1"
		port = 5000

		my_socket = socket.socket()
		my_socket.connect((host, port))

		message = input("->")
		while message != "":
			my_socket.send(message.encode('utf-8'))
			data = my_socket.recv(1024).decode('utf-8')
			print("Received from server: ", data)
			message = input("->")
		my_socket.close()		


x = TcpClient()
if __name__ == "__main__":
	x.Main()
