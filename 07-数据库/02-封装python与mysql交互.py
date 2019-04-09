#encoding=utf8
import pymysql

class MysqlHelp(object):
	
	def __init__(self,host,user,password,db='db',port=3306,charset='utf8'):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.db = db
		self.charset = charset
	
	def connect(self):
		self.db = pymysql.connect(self.host,self.user,self.password,self.db,self.port,charset=self.charset)
		self.cursor = self.db.cursor()
		print('connect')
	
	def close(self):
		self.cursor.close()
		self.db.close()
		# 
		# self.db.commit()


	def cud(self, sql, params):
		try:
			self.connect()
			self.cursor.execute(sql, params)
			self.close()
			print('ok')
		except Exception as error:
			self.db.rollback()

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
			return result

		except Exception as error:
			pass
			
			
if __name__ == '__main__':
	db = MysqlHelp("localhost", "root","zbw5688099","test1" )
	sql = 'select * from student where id=2'
	data = db.searchOne(sql)
	print(data)


