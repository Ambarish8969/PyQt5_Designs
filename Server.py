import socket
# Create a socket.
s=socket.socket()
print("Socket Created.")

# Bind it
s.bind((socket.gethostname(),8888))

s.listen(1)
print("Waiting for the connection....")

while True:
    c,address=s.accept()
    print("Connected with ", address)

    c.send(bytes("Welcome Ambi.","utf-8"))

    c.close()