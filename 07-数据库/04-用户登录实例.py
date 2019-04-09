#encoding=utf-8
from pack import MysqlHelp
from hashlib import sha1


if __name__=='__main__':
	db = MysqlHelp("localhost", "root","zbw5688099","test1" )

	clickType=input('1：登录 2：注册')
	uname=input('请输入您的用户名')
	upwd=input('请输入您的密码')

	s1=sha1()
	# s1.update(upwd.encode('utf8'))
	s1.update(upwd.encode('utf8'))
	upwdSha1=s1.hexdigest()

	sql='select upwd from userInfos where uname=%s'
	params=[uname]
	userInfo=db.searchOne(sql, params)

	# db.cud("inster into userInfos(uname,upwd) values('zbw','123')")
	print(userInfo)
	# 登录
	if clickType=='1':
		if userInfo==None:
			print('用户名错误')
		elif userInfo[0]==upwdSha1:
			print('登录成功')
		else:
			print('密码错误')
	# 注册
	elif clickType=='2':
		if userInfo !=None:
			print('用户名存在')
		else:
			sql="insert into userInfos(uname,upwd) values(%s,%s)"
			params=[uname,upwdSha1]
			db.cud(sql,params)
		
