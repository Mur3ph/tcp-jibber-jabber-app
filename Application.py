__author__="Paul"
from Client import TcpClient
from Server import TcpServer

class App():

	def Main(self):
		print("Transmission Communication Protocol (TCP)")
		
		x = TcpClient()
		y = TcpServer()

		y.Main()
		x.Main()


x = App()
if __name__ == "__main__":
	x.Main()


