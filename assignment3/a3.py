import math
import socket
import threading

isser = raw_input()

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def send_mess(a):
    while 1:
        mess = raw_input()
        a.send(mess)
    
    
def get_mess(a):
    data = a.recv(BUFFER_SIZE)
    print data
    
if isser == 's':
    s.bind((TCP_IP, TCP_PORT))
    s.listen(1)
    
    conn, addr = s.accept()
#    print 'Connection address:', addr
    while 1:
        get_mess(conn)
        send_mess(conn)  # echo
    conn.close()

    
else:

  
    
    s.connect((TCP_IP, TCP_PORT))
    send_mess(s)
    data = s.recv(BUFFER_SIZE)
#    s.close()
    
    print "received data:", data
    
    
    