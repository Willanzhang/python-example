#coding:utf-8
def shell_sort(alist):
	"""希尔排序"""
	n = len(alist)
	gap = n // 2 #python3  9//2 = 4   python2 9/2 = 4

	# gap变化到0之前插入算法执行的次数
	while gap > 0:
		# 希尔算法，与普通的插入算法的区别就是gap步长
		for j in range(gap, n):
			# j = [gap+1, gap+2， gap+3, gap+4, ...., n-1]
			i = j
			while i > 0:
				if alist[i] < alist[i - gap]:
					alist[i], alist[i - gap] = alist[i - gap], alist[i]
					i -= gap
				else:
					break
		# 缩短gap步长			
		gap //= 2
	
	print(alist)

if __name__ == "__main__":
	alist = [32,41,12,31,21,3,1,3,4,6]
	shell_sort(alist)