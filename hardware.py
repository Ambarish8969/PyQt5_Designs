# Server Program.
import socket as sk
s=sk.socket()
s.bind(("localhost",56670))
s.listen(5)
while True:
    c, addr=s.accept()
    c.send(bytes("connection successful","utf-8"))  
    while True:
        data=c.recv(1024).decode()
        if data=="700":
            new_data=int(data)+8
            c.send(bytes(str(new_data),"utf-8"))
        elif data=="900":
            new_data=int(data)+8
            c.send(bytes(str(new_data),"utf-8"))
        c.close()    