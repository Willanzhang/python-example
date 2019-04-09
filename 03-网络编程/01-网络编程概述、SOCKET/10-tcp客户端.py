from socket import *

tcpClientSocket = socket(AF_INET, SOCK_STREAM)

tcpClientSocket.connect(('192.168.50.66', 8989))

tcpClientSocket.send('你好呀'.encode('gb2312'))

recvData = tcpClientSocket.recv(1024)

print('recvData:%s'%recvData)

tcpClientSocket.close()