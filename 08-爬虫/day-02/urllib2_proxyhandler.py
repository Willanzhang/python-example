#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import config

print config.config

# 代理开关，表示是否启用代理
proxyswitch = True

# 构建一个Handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器IP+PROT
# httpproxy_handler = urllib2.ProxyHandler({"http" : "122.136.212.132:53281"})
httpproxy_handler = urllib2.ProxyHandler({"http" : "172.16.211.38:8100"})

# 构建了一个没有代理的处理器对象
nullproxy_handler = urllib2.ProxyHandler({})

if proxyswitch:
    opener = urllib2.build_opener(httpproxy_handler)
else:
    opener = urllib2.build_opener(nullproxy_handler)

# 只使用一次 opener.open(request)

# 构建了一个全局的opener，之后所有的请求都可以用 urlopen()方式去发送，也附带 Handler 的功能
urllib2.install_opener(opener)

request = urllib2.Request("http://www.baidu.com/")
response = urllib2.urlopen(request)

#若代理服务器是 gbk输出 decode('gbk')
# print response.read().decode("gbk")
print response.read()
