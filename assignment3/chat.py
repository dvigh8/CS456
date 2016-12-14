# telnet program example
from socket import *
import sys, threading, time, select, string, my_rsa, my_des

ans, name, port, p_name = raw_input('server (s) client (c) '), raw_input('Enter your name: '), int(raw_input('port number: ')), ''
n, e, d = 0, 0, 0

if ans == 's':
	s = socket(AF_INET, SOCK_STREAM)
	s.bind(('', port))
	s.listen(1)
	sckt, addr = s.accept()
	n, e, d = my_rsa.key_gen()
	print 'n: ' + str(n)
	print 'e: ' + str(e)
	sckt.send(str(n))
	time.sleep(.1)
	sckt.send(str(e))
	key = ''
	message = sckt.recv(4096)
	while message != 'end':
		key += chr(pow(int(message),d,n))
		message = sckt.recv(4096)
	print 'DES key: ' + key
	
else:
	sckt = socket(AF_INET, SOCK_STREAM)
	host = raw_input('host: ')
	server_address = (host, port)
	sckt.connect((server_address))
	n = int(sckt.recv(4096))
	print 'n: ' + str(n)
	e = int(sckt.recv(4096))
	print 'e: ' + str(e)
	key = raw_input('Enter DES key: ')
	for i in range(len(key)):
		sckt.send(str(pow(ord(key[i]),e,n)))
		time.sleep(.1)
	sckt.send('end')
		
my_des.def_key(key)
		
# name exchange
if ans == 's':
	sckt.send(my_des.encrypt(name))
	ans = sckt.recv(4096)
	p_name =  my_des.decrypt(ans)
else:
	ans = sckt.recv(4096)
	p_name =  my_des.decrypt(ans)
	sckt.send(my_des.encrypt(name))
print 'You are now talking with ' + p_name + '.'
name += ': '
p_name += ': '
	
def getMessage():
	sys.stdout.write(name)
	sys.stdout.flush()

def send():
	while True:
		message = sys.stdin.readline()
		sckt.send(my_des.encrypt(message))
		getMessage()

def recv():
	while True:
		reply = sckt.recv(4096)
		sys.stdout.write('\r' + p_name + my_des.decrypt(reply))
		getMessage()

one = threading.Thread(target = send)
two = threading.Thread(target = recv)
one.daemon = True
two.daemon = True
one.start()
two.start()
getMessage();
while True:
	time.sleep(1)