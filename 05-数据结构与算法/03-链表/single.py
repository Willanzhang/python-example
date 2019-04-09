# coding:utf-8
class Node(object):
	"""节点"""
	def __init__(self, elem):
		self.elem = elem
		self.next = None

node = Node(1000)   

class SingleLinkList(object):
	"""单链表"""
	def __init__(self):
		self.__head = None

	#  链表是否为空
	def is_empty(self):
		return self.__head == None

	# 链表长度
	def length(self):
		count = 0
		current = self.__head
		while current != None:
			count += 1
			current = current.next

		return count

	# 遍历整个链表
	def travel(self):
		current = self.__head
		while current != None:
			print(current.elem, end=' ')
			current = current.next
		# print('\n')

	
	# 链表头部添加元素 头插法
	def add(self,item):
		node = Node(item)
		node.next = self.__head
		self.__head = node
	
	# 链表尾部添加元素 尾插法
	def append(self, item):
		node = Node(item)
		if self.is_empty():
		  self.__head = node
		else:
		  current = self.__head
		  while current.next != None:
			  current = current.next
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
		cur = self.__head
		pre = None
		while cur !=None:
			if cur.elem == item:
				if pre == None:
					self.__head = cur.next
				else: 
					pre.next = cur.next
				break
			else:
				pre = cur
				cur = cur.next
		
	
	# 查找节点是否存在
	def search(self,item):
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				return True
			else:
				cur = cur.next
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

