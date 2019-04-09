#encoding=utf8
import pymysql

class MysqlHelp(object):
	
	def __init__(self,host,user,password,db1='db',port=3306,charset='utf8'):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.db1 = db1
		self.charset = charset
	
	def connect(self):
		self.db = pymysql.connect(self.host,self.user,self.password,self.db1,self.port,charset=self.charset)
		self.cursor = self.db.cursor()
		print('connect')
	
	def close(self):
		self.cursor.close()
		self.db.close()
		# self.db.commit()


	def cud(self, sql, params=()):
		count=0
		try:
			self.connect()
			count=self.cursor.execute(sql, params)
			self.db.commit()
			self.close()
			print('ok')
		except Exception as error:
			print('cud',error)
			# self.db.rollback()
			# self.close()
		return count

	def searchAll(self, sql, params=()):
		try:
			self.connect()
			self.cursor.execute(sql, params)
			result =self.cursor.fetchall()
			self.close()
			print(1)
			print('searchAll')
			return result
		except Exception as error:
			print(error)

	def searchOne(self, sql, params=()):
		try:
			self.connect()

			self.cursor.execute(sql, params)
			result = self.cursor.fetchone()
			self.close()
			print('close')
			return result
		except Exception as error:
			pass
			
			


