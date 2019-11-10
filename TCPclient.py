import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating socket object
host = socket.gethostname()
port = 2562
clientsocket.connect((host, port)) #connecting to the server
complete_info = '' #complete information to be recieved, variable with an empty string
while True:
        message = clientsocket.recv(10)
        if len (message)<=0:
            break
        complete_info += (message.decode("utf-8")) #decoding the message in utf8 bytes
print(complete_info)
