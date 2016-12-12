# telnet program example
from socket import *
import sys, threading, time, select, string, my_rsa
ans = raw_input('server (s) client (c) ')
name = raw_input('Enter your name: ')
name += ': '
n = 0
e = 0
d = 0
if ans == 's':
	s = socket(AF_INET, SOCK_STREAM)
	s.bind(('', 13699))
	s.listen(1)
	sckt, addr = s.accept()
	
else:
	sckt = socket(AF_INET, SOCK_STREAM)
	server_address = ('localhost', 13699)
	sckt.connect((server_address))
def getMessage():
	sys.stdout.write(name)
	sys.stdout.flush()

def client_send():
	while True:
		message = sys.stdin.readline()
		sckt.send(name + message)
		getMessage()
		

def client_recv():
	while True:
		reply = sckt.recv(4096)
		sys.stdout.write('\r' + reply)
		getMessage()

# key exchange
if ans == 's':
	n, e, d = my_rsa.key_gen()
	print 'n: ' + str(n)
	print 'e: ' + str(e)
	sckt.send(str(n).encode())
	time.sleep(.1)
	sckt.send(str(e).encode())
	key = ''
	message = sckt.recv(4096).decode()
	while message != 'end':
		key += chr(pow(int(message),d,n))
		message = sckt.recv(4096).decode()
	print 'DES key: ' + key
else:
	n = int(sckt.recv(4096).decode())
	print 'n: ' + str(n)
	e = int(sckt.recv(4096).decode())
	print 'e: ' + str(e)
	key = raw_input('Enter DES key: ')
	for i in range(len(key)):
		sckt.send(str(pow(ord(key[i]),e,n)).encode())
		time.sleep(.1)
	sckt.send('end'.encode())

one = threading.Thread(target = client_send)
two = threading.Thread(target = client_recv)
one.daemon = True
two.daemon = True
one.start()
two.start()
getMessage();
while True:
	time.sleep(1)