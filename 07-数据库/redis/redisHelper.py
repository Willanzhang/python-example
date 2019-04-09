#coding=utf-8
from redis import *

class redisHelper():
	def __init__(self,host,port):
		self.__redis=StrictRedis(host,port)

	def set(self, key, value):
		self.__redis.set(key,value)
	
	def get(self, key):
		return self.__redis.get(key)
