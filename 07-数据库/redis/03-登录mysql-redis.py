#coding=utf-8
from pack import MysqlHelp
from hashlib import sha1
from redisHelper import redisHelper

if __name__ == '__main__':
	#接收输入
	clickType=input('1：登录 2：注册')
	name=input('请输入用户名')
	pwd1=input('请输入密码')

	#加密
	s1=sha1()
	s1.update(pwd1.encode('utf-8'))
	pwd=s1.hexdigest()

	#查询redis中是否存在此用户
	r=redisHelper('localhost', 6379)
	
	db = MysqlHelp("localhost", "root","zbw5688099","test1" )


	if clickType == '1':
		redisUname = r.get('uname')

		# 若redis中没有保存
		if redisUname == None:

			sql='select upwd from userInfos where uname=%s'
			params=[name]
			userInfo=db.searchOne(sql, params)
			# 查询信息为空
			if userInfo == None:
				print('用户名错误')
			else:
				#只要查询到 就在redis中写入
				r.set(name, userInfo[0])
				#判断密码是否登录成功
				if userInfo[0] == pwd:
					print('登录成功')
				else:
					print('密码错误')
		# redis 存有次用户
		else:
			# 是否输入等于redis中存入的密码
			if pwd == r.get(name):
				print('登录成功')
			else:
				print('密码错误')
	
	# 若是注册
	elif clickType == '2':
		
		sql='select upwd from userInfos where uname=%s'
		params=[name]
		userInfo=db.searchOne(sql, params)

		if userInfo !=None:
			print('用户名存在')
		else:
			sql="insert into userInfos(uname,upwd) values(%s,%s)"
			params=[name,pwd]
			db.cud(sql,params)
		
			
