#coding = 'utf-8'
# 99乘法表
# i = 1
# while i <= 9:
# 	j = 1
# 	s= ''
# 	while j <= i:
# 		s += '%d * %d \t'%(j,i)
# 		j += 1
# 	i += 1
# 	print(s,'\n')

# 素数
# s = []
# i = 100
# while i <= 200:
# 	l = 0
# 	j = 1
# 	while j <= i:
# 		if i%j == 0:
# 			l += 1
# 		j += 1
# 	if l <= 2:
# 		s.append(i)
# 	i += 1

# print('100-200之间素数有', s)	


# year = int(input('请输入年份'))
# if year%400==0 or year%4==0 and year%100 != 0:
# 	print('是闰年')  
# else:
# 	print('不是')


# def judDay() {
# 	time = input('请按照如下格式输入年月日- 20180101')
# 	isMore = 0
# 	totalDay = 0
# 	year = int(day[0:5])
# 	month = int(day[5:7])
# 	day = int(day[7:9])
# 	if year%400==0 or year%4==0 and year%100 != 0:
# 		isMore = 1 
# 	else:
# 		isMore = 0
# 	if month == 1:
# 		totalDay += 31
# 	elif month == 2:
# 		if isMore == 1:
# 			totalDay = 31 + 2
# }


# 备份
f_name = input('请输入你想要的文件名')
index = f_name.rfind('.')
new_name = f_name[:index] + '[复制]' + f_name[index:]
f = open(f_name, 'r')
f1 = open(new_name, 'w')

# 1
# for lineContent in f.readlines():
# 	f1.write(lineContent)

# 2
# f1.write(f.read())

# 3
# while True:
# 	lineContent = f.readline()
# 	if len(lineContent) > 0:
# 		f1.write(lineContent)
# 	else:
# 		break
f.close()
f1.close()
