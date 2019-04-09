from socket import *

#1. 创建套接字
udpSocket = socket(AF_INET, SOCK_DGRAM)

#2. 准备接收⽅的地址
sendAddr = ('192.168.153.1', 8080)

#3. 从键盘获取数据

#4. 发送数据到指定的电脑上
udpSocket.sendto(b'hehhe', sendAddr)
# 或者udpSocket.sendto(b'hehhe'.encode(), sendAddr)
# python2 就不需要像上面那样加 b  或者encode

    
#5. 关闭套接字
udpSocket.close()