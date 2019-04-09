from pack import MysqlHelp

if __name__=='__main__':
	db = MysqlHelp("localhost", "root","zbw5688099","test1" )
	sql = "insert into student values(0, %s,%s)"
	params=['zbw', 'zbw']
	data = db.cud(sql,params)
	print(data)
  