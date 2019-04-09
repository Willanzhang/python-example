#coding:utf-8

def bubble_sort(alist):
	"""冒泡排序"""
	n = len(alist)
	for j in range(0, n-1):
		for i in range(0, n-1-j):
			if alist[i] >= alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]
	print(alist)
a = [51,31,51,1,3,2,5,6,99]
bubble_sort(a)