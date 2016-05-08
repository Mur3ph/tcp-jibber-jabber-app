__author__ = "Paul"
import socket

class TcpServer():

	def Main(self):
		print("TcpServer")
		host = "127.0.0.1"
		port = 5000
		
		my_socket = socket.socket()
		my_socket.bind((host, port))

		my_socket.listen(1)
		client, addr = my_socket.accept()
		
		print("Connection from: " + str(addr))

		while True:
			data = client.recv(1024).decode('utf-8')
			if not data:
				break
			print("From connected user: " + data)
			data = data.upper()
			print("Sending data in UPPER case to Client: ", data)
			client.send(data.encode('utf-8'))
		client.close()


x = TcpServer()
if __name__ == "__main__":
	x.Main()
