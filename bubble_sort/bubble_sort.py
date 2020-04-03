def bubble_sort(li):
	"""
	冒泡排序
	:param li:数组
	"""
	# 倒序遍历数组的index
	for ind in range(len(li))[::-1]:
		# 令本次数组的最大值的index为0
		max_index = 0
		# 去出数组的前ind+1个，即i的取值为0-ind
		for i in range(ind+1):
			# 如果index为i的值大于index为max_index的值，则将i赋值给max_index
			if li[i] > li[max_index]:
				max_index = i
		# 交换最大值的index给数组的末尾
		li[ind], li[max_index] = li[max_index], li[ind]


if __name__ == '__main__':
	li = [5, 2, 9, 10, 7, 3, 1]
	bubble_sort(li)
	print(li)
