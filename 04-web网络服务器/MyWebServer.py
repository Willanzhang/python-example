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

		def __init__(self, application):
				"""构造函数 application指的是框架的app"""
				self.serverSocket = socket(self.addressFamialy, self.socketType)
				self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
				# self.serverSocket.bind(address)
				self.app = application

		def start(self):
				self.serverSocket.listen(self.listenQueueSize)
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
				
				if len(requestData) < 1:
						return print('110')
				requestHeader = requestData[0]
				fileName = re.match(r"\w+ +(/[^ ]*) ", requestHeader.decode('utf-8')).group(1)
				method = re.match(r"(\w+) +/[^ ]*", requestHeader.decode('utf-8')).group(1)

				param = ''
				# WSGI定义了我们需要传的字符 有很多个
				env = {
						"PATH_INFO": fileName,
						"METHOD": method
				}

				responseBody = self.app(env, self.startResponse)

				response = self.responseHeaders + "\r\n" + responseBody

				clientSocket.send(bytes(response, 'utf-8'))
				clientSocket.close()

		def bind(self, port):
				self.serverSocket.bind(("", port))

def createServer(address):
		server = WSGIServer(address)
		return server

def main():
		sys.path.insert(1, WSGI_PYTHON_DIR)  # 添加导入包的路径
		if len(sys.argv) < 2:
				sys.exit("python MyWebServer.py Moudle:app")

		# python3 MyWebServer.py MyWebFramework:app
		sys.argv #!
		module_name, app_name = sys.argv[1].split(":")
		# module_name = MyWebFramework
		# app_name = app
		m = __import__(module_name)
		print(m)

		# getarttr(m, 'Application)  从模块中获取属性 或者对象
		app = getattr(m, app_name)

		# app = Application(urls)

		httpd = createServer(app)
		httpd.bind(7788)
		httpd.start()

if __name__ == '__main__':
		main()