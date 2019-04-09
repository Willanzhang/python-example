from socket import *

# 创建套接字
serSocket = socket(AF_INET, SOCK_STREAM)

#绑定ip 以及port
desAddrs = ('', 7788)
serSocket.bind(desAddrs)

#让这个socket 变为非阻塞
serSocket.setblocking(False)

#3 将socket 变为监听（被动）套接字
serSocket.listen(100)
clientAddrList = []


while True:
    try:
        # 等待新的客户端到来（即完成三次握手的客户端）
        clientSocket, destAddr = serSocket.accept()
    except:
        pass
    else:
        clientSocket.setblocking(False)
        clientAddrList.append((clientSocket, destAddr))
        print("一个新的客户端到来：%s"%str(destAddr))
        
    for clientSocket, destAddr in  clientAddrList:
        try:
            recvData = clientSocket.recv(1024)
        except:
            pass
        else:
            if len(recvData) > 0:
                print("%s:%s"%(str(destAddr),recvData))
            else:
                clientSocket.close()
                clientAddrList.remove((clientSocket, desAddrs))
                print("%s已经下线"%desAddrs)
