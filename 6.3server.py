import socket
import math
import sys
import time 
import errno
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 Not Found \n\n'


def process_start(s_sock):
	s_sock.send(str.encode("[SUCCESS] Connected to Server...\n"))
	while True:
		ans = s_sock.recv(2048).decode("utf-8").split(":")

		if ans[0] == "A" :
			result = math.log(float(ans[1]))

		elif ans[0] == "B":
			result = math.sqrt(float(ans[1]))

		elif ans[0] == "C":
			result = math.exp(float(ans[1]))

		elif ans[0] == "X":
			break

		s_sock.sendall(str.encode(str(result)))
	s_sock.close()

if __name__ == '__main__':

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('',8080))
	print("[LISTEN] Listening...")
	s.listen(3)

try:
	while True:
		try:
			s_sock,s_addr = s.accept()
			print("\[CONNECT] Connection from : ", s_addr)
			p = Process(target = process_start,args = (s_sock,))
			p.start()

		except socket.error:
			print('got an error for socket')

except Exception as e:
	print('an exception occured!')
	print(e)

