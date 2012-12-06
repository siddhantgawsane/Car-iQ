from socket import *
 
HOST = ''    #we are the host
PORT = 29876    #arbitrary port not currently in use
ADDR = (HOST,PORT)    #we need a tuple for the address
BUFSIZE = 4096    #reasonably sized buffer for data
 
mysock = socket( AF_INET,SOCK_STREAM)    
 
mysock.bind((ADDR))  #bind port to socket #the double parens are to create a tuple with one element
mysock.listen(1)    #1 is the maximum number of queued connections we'll allow
print 'listening...'
 
conn,addr = mysock.accept() #accept the connection
print '...connected!'

data = 'abc'
while data!='exit':
	print 'Enter your message here : '
	data = raw_input()
	conn.send(data)
 
	if data=='exit': break	
	data = conn.recv(BUFSIZE)
	print 'client says : '
	print data

conn.close()
