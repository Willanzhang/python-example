# coding:utf-8

# 动态web服务器案例 class 版本 
import re
from multiprocessing import Process
from socket import *
import sys

HTML_ROOT_DIR =  "./html"# HTML 根路径
WSGI_PYTHON_DIR = "./wsgipython"

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
    
    def startResponse(self, status, headers):
        serverHeaders = [
            ("Server", "My Server")
        ]
        responseHeaders = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            responseHeaders += "%s: %s\r\n"%header
        self.responseHeaders = responseHeaders

    def dealCilentRequest(self, clientSocket):
        recvData = clientSocket.recv(1024)
        requestData = recvData.splitlines()
        for line in requestData:
            print(line)
        requestHeader = requestData[0]
        fileName = re.match(r"\w+ +(/[^ ]*) ", requestHeader.decode('utf-8')).group(1)
        method = re.match(r"(\w+) +/[^ ]*", requestHeader.decode('utf-8')).group(1)

        param = ''
        # WSGI定义了我们需要传的字符 有很多个
        env = {
            "PATH_INFO": fileName,
            "METHOD": method
        }
        # "/time.py"
        if fileName.endswith(".py"):
            try:
                # 执行py文件
                m = __import__(fileName[1:-3])
                responseBody = m.application(env, self.startResponse)
            except:
                responseBody = "this is file is not found"
                self.responseHeaders = "HTTP/1.1 404 找错人了吧\r\n"

            finally:
                response = self.responseHeaders + "\r\n" + responseBody

        else:
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

            except IOError:
                data = "this is file is not found"
                responseLine = "HTTP/1.1 404 找错人了吧\r\n"
            finally:
                response = responseLine + '\r\n' +  data
        
        clientSocket.send(bytes(response, 'utf-8'))
        clientSocket.close()

def createServer(address):
    server = WSGIServer(address)
    return server

def main():
    sys.path.insert(1, WSGI_PYTHON_DIR)  # 添加导入包的路径
    httpd = createServer(('', 7788))
    httpd.serverForever()

if __name__ == '__main__':
    main()