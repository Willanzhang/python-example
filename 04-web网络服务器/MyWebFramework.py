# coding:utf-8

import time
from MyWebServer import WSGIServer
HTML_ROOT_DIR = "./html"

class Application(object):

		def __init__(self, urls):
				self.urls = urls

		def __call__(self, env, startResponse):
				path = env.get("PATH_INFO", "/")  # 第二个参数 是默认值。
				# 判断静态文件  /static/ 开头
				if path.startswith("/static"):
					# 要访问静态文件
					fileName = path[7:]

					if "/" == fileName:
							fileName = HTML_ROOT_DIR + '/index.html'
					else:
							fileName = HTML_ROOT_DIR + fileName

					try:
							file = open(fileName, 'rb')

					except IOError:
							status = "404 NotNot Found"
							headers = []
							startResponse(status, headers)
							return "Not Found"
					else:
							data = file.read().decode('utf-8')
							file.close()

							status = "200 OK"
							headers = []
							startResponse(status, headers)
							return data

				for url, handler in self.urls:
						if path == url:
								return handler(env, startResponse)

				status = "404 NotNot Found"
				headers = []
				startResponse(status, headers)
				return "Not Found"       

def showTime(env, startResponse):
		status = "200 ok"
		headers = [
			("Content-Type", "text/plain"),
			("Server", "My Server"),
		]
		startResponse(status, headers)
		return time.ctime()

def sayHello(env, startResponse):
		status = "200 ok"
		headers = [
			("Content-Type", "text/plain"),
			("Server", "My Server"),
		]
		startResponse(status, headers)
		return "hello william"

urls = [
	("/ctime", showTime),
	("/sayHello", sayHello)
]

# app = Application(urls)

if __name__ == "__main__":
		urls = [
		  ("/ctime", showTime),
		  ("/sayHello", sayHello)
		]
		app = Application(urls)
		http_server = WSGIServer(app)
		http_server.bind(7788)
		http_server.start()
