from socket import *
from multiprocessing import *
from time import sleep

def dealWithClinet(newSocket, destAddr):
    while True:
        recvData = newSocket.recv(1024)
        if len(recvData)> 0:
            print('recv[%s]:%s'%(str(destAddr),  recvData))
        else: 
            print('[%s]客户端已经关闭'%str(destAddr))
            break
    newSocket.close()


def main():
    serSocket = socket(AF_INET, SOCK_STREAM)

    # 重复使用绑定的信息
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    localAddr = ('', 7788)

    serSocket.bind(localAddr)

    serSocket.listen(5)

    try:
        while True:
            print('-------主进程，，等待新客户端的到来--------')

            newSocket, destAddr = serSocket.accept()

            client = Process(target=dealWithClinet, args=(newSocket, destAddr))
            
            client.start()

            newSocket.close()
            print('-------主进程，，接下来负责数据的处理【%s】-------'%str(destAddr))
    finally:
        serSocket.close()

if __name__ == '__main__':
    main()