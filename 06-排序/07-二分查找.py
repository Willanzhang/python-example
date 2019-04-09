#coding:utf-8
def binary_search(alist, item):
	"""二分查找,递归"""
	n = len(alist)
	if n > 0:
		mid = n // 2
		if alist[mid] == item:
			return True
		elif item < alist[mid]:
			return binary_search(alist[:mid], item)
		else:
			return binary_search(alist[mid+1:], item)
	return False

# def merge()
def binary_search(alist, item):
	"""二分查找， 非递归"""
	n = len(alist)
	first = 0
	last = n - 1 
	while first <= last:
		mid = (first + last)//2
		if alist[mid] == item:
			return True
		elif item < alist[mid]:
			last = mid -1
		else:
			first = mid + 1
	return False

if __name__ == "__main__":
	alist = [1,2,3,4,5,6,11, 22, 33, 44, 55]
	print(binary_search(alist, 5))
	print(binary_search(alist, 15))
