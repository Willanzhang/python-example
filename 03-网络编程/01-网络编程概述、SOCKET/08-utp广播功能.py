from socket import *

# 也可以写成('192.168.1.255', 8080) 但是就只可以在192.168.1 这个网段使用  使用<broadcast>是表示在当前网段使用
dest = ('<broadcast>', 8181)

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.setsockopt(SOL_SOCKET, SO_BROADCAST,1)

udpSocket.sendto(b"Hello", dest)

print('等待对方回复（按 ctrl+c退出）')