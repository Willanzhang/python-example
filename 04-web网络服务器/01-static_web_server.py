# coding:utf-8

from multiprocessing import Process

from socket import *

HTML_ROOT_DIR =  "./html"# HTML 根路径


def handleClient(socket):
    # 接受请求
    requst_data = socket.recv(1024)
    # 解析http 报文数据
    # 提取请求方式
    # 提取请求路径path
    try:
        file = open(HTML_ROOT_DIR + '/index.html')
        data = file.read()
        file.close()
    except IOError:
        # 修改报文
        pass
    responseHeaderLines = "HTTP/1.1 200 OK\r\n"
    responseHeaderLines += "Server: My server\r\n"
    responseHeaderLines += "content-type: text/html; charset=UTF-8\r\n"
    responseHeaderLines += "\r\n"
    responseBody = data
    response = responseHeaderLines + responseBody

    # for line in requst_data.splitlines():
    #     print(line)
    print(requst_data.splitlines()[0])
    # 返回响应数据 满足http协议

    """
    HTTP1.1 200 OK\r\n
    \r\n
    hello world
    """
    socket.send(bytes(response, 'utf-8'))
    socket.close()
    # send
    # close
    

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # 重复使用绑定的信息
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    addressIP = ('', 7788)
    serverSocket.bind(addressIP)
    serverSocket.listen(128)
    clinetList = []
    while True:
        clientS, destAddr = serverSocket.accept()
        clinetList.append(clientS)
        print(11)
        t = Process(target=handleClient, args=(clientS,))
        t.start()
        clientS.close()

if __name__ == '__main__':
    main()