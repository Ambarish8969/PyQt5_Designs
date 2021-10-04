import socket

c=socket.socket()
c.connect((socket.gethostname(),8888))

print(c.recv(1024).decode())