from socket import *

#1. 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#2. 准备接收⽅的地址

udpSocket.bind(('192.168.50.182', 7788))

# sendAddr = ('192.168.153.1', 8080)

#3. 从键盘获取数据

#4. 接收
recvDate = udpSocket.recvfrom(1024)
# 或者udpSocket.sendto(b'hehhe'.encode(), sendAddr)
# python2 就不需要像上面那样加 b  或者encode

print(recvDate)