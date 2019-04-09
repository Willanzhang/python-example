#coding:utf-8

def select_sort(alist):
	"""选择排序"""
	n = len(alist)
	for j in range(0, n-1):
		min_index = j
		for i in range(j+1, n):
			if alist[min_index] > alist[i]:
				min_index = i
		alist[j], alist[min_index] = alist[min_index], alist[j]
	print(alist)

if __name__ == "__main__":
	alist = [32,41,12,31,21,3,1,3,4,6]
	select_sort(alist)