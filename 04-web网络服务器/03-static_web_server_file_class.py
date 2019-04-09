# coding:utf-8

# web服务器案例 class 版本
import re
from multiprocessing import Process
from socket import *

HTML_ROOT_DIR =  "./html"# HTML 根路径

class WSGIServer(object):
    addressFamialy = AF_INET
    socketType = SOCK_STREAM
    listenQueueSize = 128

    def __init__(self, address):
        self.serverSocket = socket(self.addressFamialy, self.socketType)
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.serverSocket.bind(address)
        self.serverSocket.listen(self.listenQueueSize)

    def serverForever(self):
        while True:
            self.clientSocket, self.clinetAddress = self.serverSocket.accept()
            self.multiProcesss = Process(target=self.dealCilentRequest, args=(self.clientSocket,))
            print('[%s,%s]:客户端访问'%self.clinetAddress)
            self.multiProcesss.start()
            self.clientSocket.close()
    
    def dealCilentRequest(self, clientSocket):
        recvData = clientSocket.recv(1024)
        requestData = recvData.splitlines()
        for line in requestData:
            print(line)
        requestHeader = requestData[0]
        fileName = re.match(r"\w+ +(/[^ ]*) ", requestHeader.decode('utf-8')).group(1)

        if "/" == fileName:
            fileName = HTML_ROOT_DIR + '/index.html'
        else:
            fileName = HTML_ROOT_DIR + fileName

        responseLine = "HTTP/1.1 200 OK\r\n"
        
        try:
            file = open(fileName, 'rb')
            data = file.read().decode('utf-8')
            file.close()
            responseLine += "Server: My server\r\n"
            responseLine += "content-type: text/html; charset=UTF-8\r\n"

        except:
            data = "this is file is not found"
            responseLine = "HTTP/1.1 404 找错人了吧\r\n"
        
        clientSocket.send(bytes(responseLine + '\r\n' +  data, 'utf-8'))
        clientSocket.close()

def createServer(address):
    server = WSGIServer(address)
    return server

def main():
    httpd = createServer(('', 7788))
    httpd.serverForever()

if __name__ == '__main__':
    main()