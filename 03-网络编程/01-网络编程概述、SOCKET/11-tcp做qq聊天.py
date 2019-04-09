from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

address = ('', 8899)
serverSocket.bind(address)

serverSocket.listen(5)

while True:
    

