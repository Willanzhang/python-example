#coding:utf-8
def quick_sort(alist, start, end):
	"""快速排序"""
	if start >= end :
		return

	mid_value = alist[start]
	low = start
	high = end
	while low < high:
		# high 左移
		while low < high and alist[high] >= mid_value:
			high -= 1
		alist[low] = alist[high] 

		# low 右移
		while low < high and alist[low] < mid_value:
			low += 1
		alist[high] = alist[low]

	alist[low] = mid_value
	
	quick_sort(alist, start, low-1)
	quick_sort(alist, low+1, end)
	# quick_sort(alist[:low-1])
	# quick_sort(alist[low+1:])

	

if __name__ == "__main__":
	alist = [32,41,12,31,21,3,1,3,4,6]
	quick_sort(alist, 0, len(alist)-1)
	print(alist)