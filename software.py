# Client Program.
import time
import socket as sk
s=sk.socket()
s.connect(("localhost", 5667))

print("Waiting for connection")
time.sleep(5)
print(s.recv(1024).decode())
data=700
s.send(bytes(str(data),"utf-8"))
print(s.recv(1024).decode())
