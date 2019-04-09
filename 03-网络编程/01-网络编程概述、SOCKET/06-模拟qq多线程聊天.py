from socket import *
import threading

def recvfrom(udpSocket):
    while True:
        info = udpSocket.recvfrom(1024)
        if info:
            print('\r收到来自%s的信息：%s'%(str(info[1]), info[0].decode('gb2312')), )
            print('<<',end = '')

def recvto(udpSocket):
    while True:
        disgusting = input('<<')
        info = udpSocket.sendto(disgusting.encode('gb2312'), ('192.168.50.66', 8080))
        # print('发')

def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(('', 8080))
    t1 = threading.Thread(target=recvto, args=(udpSocket,))
    t2 = threading.Thread(target=recvfrom, args=(udpSocket,))
    t1.start()
    t2.start()

if __name__ == "__main__":
    main()