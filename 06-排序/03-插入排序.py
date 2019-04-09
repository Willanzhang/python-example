#coding:utf-8

def insert_sort(alist):
	"""插入排序"""
	n = len(alist)
	# 从右边的无序序列中取出多少个元素执行这样的过程
	for j in range(1, n):
		# j代表内层循环起始值
		# 执行从右边的无序序列中去除第一个元素，即j位置元素，然后将其插入到前面的正确的位置中
		while j > 0:
			if alist[j] < alist[j-1]:
				alist[j], alist[j-1] = alist[j-1], alist[j]
				j -= 1
			# 最优时间复杂度处理
			else:
				break
	print(alist)

if __name__ == "__main__":
	alist = [32,41,12,31,21,3,1,3,4,6]
	insert_sort(alist)