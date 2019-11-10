import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating socket object, SOCK_STREAM is used to create tcp protocols
host = socket.gethostname()
port = 2562
serversocket.bind((host,port)) #binding to the client, used when server and client are on the same device
serversocket.listen(5)

while True: #accept the client socket and address
    clt, adr=serversocket.accept()
    print(f"connection to {adr} successful")
    clt.send(bytes("this is a tcp socket program in python", "utf-8")) #message to client in utf8 bytes
    clt.close() #close communication
