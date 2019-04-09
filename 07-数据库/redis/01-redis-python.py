#coding=utf-8
from redis import *

#连接
try:
	r=StrictRedis(host='localhost', port=6379)
	r.set('superMan', 'william')
	r.get('name')
	pipe=r.pipeline()
	pipe.set('superMaket', 'wowo')
	pipe.execute()
except Exception as Error:
	print(Error)
