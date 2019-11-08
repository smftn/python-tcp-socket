import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating socket object
host = socket.gethostname()
port = 9999
clientsocket.connect((host, port))
message = clientsocket.recv(1024)
print(message.decode("utf-8"))