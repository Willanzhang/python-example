# coding:utf-8
class Node(object):
	"""节点"""
	def __init__(self, elem):
		self.elem = elem
		self.next = None

node = Node(1000)   

class SingleLinkList(object):
	"""单向循环链表"""
	def __init__(self, node=None):
		self.__head = None
		if node:
			node.next = node		

	#  链表是否为空
	def is_empty(self):
		return self.__head == None

	# 链表长度
	def length(self):
		if self.is_empty():
			return 0
		count = 1
		current = self.__head
		while current.next != self.__head:
			count += 1
			current = current.next

		return count

	# 遍历整个链表
	def travel(self):
		current = self.__head
		while current.next != self.__head:
			print(current.elem, end=' ')
			current = current.next
		print(current.elem)
		# print('\n')

	
	# 链表头部添加元素 头插法
	def add(self,item):
		node = Node(item)
		if self.is_empty():
			self.__head = node
			node.next = node
		else:
			current = self.__head
			while current.next != self.__head:
				current = current.next	
			# 退出循环，cur指向尾节点
			node.next = self.__head
			self.__head = node
			current.next = node

	# 链表尾部添加元素 尾插法
	def append(self, item):
		node = Node(item)
		if self.is_empty():
			self.__head = node
			node.next = node
		else:
			current = self.__head
			while current.next != self.__head:
				current = current.next
			node.next = self.__head
			current.next = node

	# 指定位置添加元素
	def insert(self, pos, item):
		"""
		:params: pos 从0开始
		"""
		if pos <= 0:
			self.add(item)
		elif pos > self.length() - 1:
			self.append(item)
		else:
		  pre = self.__head
		  count = 0
		  while count < pos - 1:
			  pre = pre.next
			  count += 1
		  # 当循环推出后 pre 指向pos-1位置
		  node = Node(item)
		  node.next = pre.next
		  pre.next = node
	
	# 删除节点
	def remove(self, item):
		if self.is_empty():
			return
		cur = self.__head
		pre = None
		while cur.next != self.__head:
			if cur.elem == item:
				if cur == self.__head:
					# 假如删除的是第一个节点
					rear = self.__head
					while rear.next != self.__head:
						rear = rear.next
					self.__head = cur.next
					rear.next = self.__head
				else: 
					pre.next = cur.next
				return
			else:
				pre = cur
				cur = cur.next
		# 退出循环，cur指向尾节点
		if cur.elem == item:
			if cur = self.__head:
				self.__head == None
			else:
				pre.next = cur.next
		
	
	# 查找节点是否存在
	def search(self,item):
		if self.is_empty():
			return False
		cur = self.__head
		while cur.next != self.__head:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
		if cur.elem == itme:
			return True
		return False

# single_obj = SingleLinkList(node)

if __name__ == "__main__":
	ll = SingleLinkList()
	print(ll.is_empty())
	print(ll.length())

	ll.append(1)
	print(ll.is_empty())
	print(ll.length())



	ll.append(2)
	ll.append(3)
	ll.append(4)
	ll.append(5)
	ll.append(6)
	ll.add(90)
	print('000000', ll.length())
	ll.travel()

