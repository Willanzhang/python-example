class Home:
	def __init__(self, area):
		self.area = area
		self.light = 'on'
		self.containsItem = []
	
	def __str__(self):
		msg = '家可用面积为：' + str(self.area)
		msg += '\n'
		msg += '家里的物品有：' 
		# msg += ''.join(self.containsItem)
		for tem in self.containsItem:
			msg += '%s,'%tem.getName() 
		msg = msg[:-1]
		if self.light == 'on':
			msg += '\t' + '当前灯是开着的，所有的物品都是可见的'
		else:
			mgs	+= '\t' + '当前灯是关着的，所有的物品都是不可见的'
		return msg

	def addItem(self, item):
		needArea = item.getArea()
		if self.area >= needArea:
			self.containsItem.append(item)
			self.area -= needArea
		else :
			print('快去买个大房间')
	
	def turnoff(self):
		self.light = 'off'
		for tem in containsItem:
			temp.turnoff()



class Bed:
	def __init__(self,name, area):
		self.name = name
		self.area = area
		self.color = 'light'

	def __str__(self):
		msg = self.name + '床的面积为：' + str(self.area)
		return msg

	def getName(self):
		return self.name

	def getArea(self):
		return self.area
		
	def turnoff(self):
		self.light = 'off'

#创建家的对象
myHome = Home(128)
#print(myHome)


bed = Bed('席梦思', 4)
print(bed)
bed1 = Bed('硬板床', 4)
print(bed1)
myHome.addItem(bed)
myHome.addItem(bed1)
print(myHome)
