#coding:utf-8
def merge_sort(alist):
	"""归并排序"""
	n = len(alist)
	if n <= 1:
		return alist
	mid = n // 2
	left = merge_sort(alist[:mid])
	right = merge_sort(alist[mid:])

	# 将两个有序的子序列合并成一个整体
	# merge(left, right)
	left_pointer, right_pointer = 0, 0
	result = []
	while left_pointer < len(left) and right_pointer < len(right):
		if left[left_pointer] <= right[right_pointer]:
			result.append(left[left_pointer])
			left_pointer += 1
		else:
			result.append(right[right_pointer])
			right_pointer += 1
	result += left[left_pointer:]
	result += right[right_pointer:]
	return result
	# print(right, end="\n")

# def merge()

if __name__ == "__main__":
	alist = [32,41,12,31,21,3,1,3,4,6]
	print(merge_sort(alist))