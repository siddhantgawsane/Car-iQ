from socket import *
 
HOST = 'localhost'
PORT = 29876    #our port from before
ADDR = (HOST,PORT)
BUFSIZE = 4096
 
mysock = socket( AF_INET,SOCK_STREAM)
mysock.connect((ADDR))

data = 'abc'
while data!='exit':
	data = mysock.recv(BUFSIZE)
	print 'server says : '
	print data

	if data=='exit': break	
	print 'Enter your message here : '
	data = raw_input()
	mysock.send(data)
 
mysock.close()
