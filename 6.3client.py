import sys
import socket

clientSocket = socket.socket()
host = '192.168.114.6'
port = 8080

print("[WAITING] Waiting for connection...")

try:
	clientSocket.connect((host,port))

except socket.error as e:
	print(str(e))


response = clientSocket.recv(1024)
print(response.decode())

while True:
	opt = input('Please Select Your Math function - [A]Log [B]Sqrt [C]Exponent [X]Exit\n')

	if opt == 'A' or opt == 'B' or opt == 'C':

		number = input("Enter a number: ")
		opt = opt + ":" + number
		clientSocket.send(str.encode(opt))
		response = clientSocket.recv(1024)
		print(response.decode("utf-8"))

	elif opt == 'X':
		print("[EXIT] exiting...")
		clientSocket.send(str.encode(option))
		sys.exit()


clientSocket.close()

