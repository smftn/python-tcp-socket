import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating socket object
host = socket.gethostname()
port = 9999
serversocket.bind((host,port))
serversocket.listen(5)

while True:
    clt, adr=serversocket.accept()
    print(f"connection to {adr} successful")
    clt.send(bytes("this is a tcp socket program in python", "utf-8"))

