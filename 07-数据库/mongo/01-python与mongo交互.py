#coding=utf-8
from pymongo import MongoClient

#获得客户端 
# 无安全认证: client=MongoClient('mongodb://localhost:27017')
# 有安全认证： client=MongoClient('mongodb://用户名:密码@localhos:27017/数据库名称') 
clinet=MongoClient('mongodb://admin:123@localhost:27017/admin')

#切换数据库
db=client.py3
#获取集合
stu.db.stu

#增加
stu.insert({'name': '张三丰'})

#修改
stu.update_one({'name': '张三丰'},{'$set': {'name': 'abc'}})

#删除
stu.delete_one({'name': 'abc'})

#查询
# cursor=stu.find({'age': {'&gt': 20}}).skip(1).limit(1)
cursor=stu.find({})
for s in cursor:
    print(s['name'])

#排序 升序ASCENDING   降序DESCENDING
# sort('age': DESCENDING)
# sort('age': -1)  #1

#基于多个条件排序
sort([('age', DESCENDING),('_id', ASCENDING)])

