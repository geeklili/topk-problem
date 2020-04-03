def select_sort_max(li):
	"""
	选择排序，选最大值
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


def select_sort_min(li):
	"""
	选择排序，选最小值，插入到最前面
	:param li: 数组
	"""
	for ind in range(len(li)):
		min_index = ind
		for i in range(ind, len(li)):
			if li[i] < li[min_index]:
				min_index = i
		li[ind], li[min_index] = li[min_index], li[ind]


if __name__ == '__main__':
	li = [5, 2, 9, 10, 7, 3, 1]
	# select_sort_max(li)
	# print(li)

	select_sort_min(li)
	print(li)
