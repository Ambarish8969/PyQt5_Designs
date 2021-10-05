import socket

s=socket.socket()
s.bind((socket.gethostname(),8080))
s.listen(2)
print("Waiting for the connection....")

while True:
    c,address=s.accept()
    print(f"Connected with : {address}")
    
    c.send(bytes("welcome bro ","utf-8"))
    
    c.close()