#encoding=utf8
import pymysql

# 打开数据库连接
# db = pymysql.connect(host="localhost",port="3306",db="test",user="root",passwd="123456", charset="utf8" )
# db = pymysql.connect("localhost","3306","test","root","123456","utf8" )
db = pymysql.connect("localhost","root","zbw5688099","test1" )
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
try:
	# cursor.execute("create table room( id int primary key not null, title varchar(10) not null);")

	# cursor.execute("create table student(id int primary key auto_increment not null,title varchar(10) not null);")

	# 参数化
	# title = input('请输入您的姓名：')
	# ui = input('请输入您的学号：')
	# print(type(ui))
	# params = {}
	# params[title] = title
	# cursor.execute("insert into student(title, ui) values(%s,%s)",(params[title], ui))
	# 参数化

	# 查询一条数据 配合sql查询使用
	# cursor.execute("select * from student where id=5")
	# data = cursor.fetchone()
	# 查询一条数据 配合sql查询使用

	# 查询所有数据 配合sql查询使用
	cursor.execute("select * from student")
	data = cursor.fetchall()
	# 查询所有数据 配合sql查询使用

	cursor.close()
	db.commit()
	print (data)

except Exception as a:
	print('rollbacjk', a)
	db.rollback()
 
# 使用 fetchone() 方法获取单条数据.
 
 
# 关闭数据库连接
db.close()