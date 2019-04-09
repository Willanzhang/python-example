# coding:utf-8
from single import SingleLinkList
class Node(SingleLinkList):
	"""节点"""
	def __init__(self, elem):
		self.elem = elem
		self.next = None
		self.prev = None

node = Node(1000)   

class DoubleLinkList(object):
	"""单链表"""
	def __init__(self):
		self.__head = None

	#  链表是否为空
	def is_empty(self):
		return self.__head is None

	# 链表长度
	def length(self):
		count = 0
		current = self.__head
		while current is not None:
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
		node.next.prev = node
			
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
			node.prev = current

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
			cur = self.__head
			count = 0
			while count < pos :
				count += 1
				cur = pre.next
			# 当循环推出后 pre 指向pos-1位置
			node = Node(item)
			node.next = cur
			node.prev = cur.prev
			cur.prev.next = node
			cur.prev = node

	
	# 删除节点
	def remove(self, item):
		cur = self.__head
		while cur != None:
			if cur.elem == item:
				if cur == self.__head:
					self.__head = cur.next
					if cur.next:
						# 判断链表是否只有一个节点
						cur.next.prev = None
				else: 
					cur.prev.next = cur.next
					if cur.next:
							cur.next.prev = cur.prev
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
	ll = DoubleLinkList()
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
	ll.remove(5)
	print('000000', ll.length())
	ll.travel()

