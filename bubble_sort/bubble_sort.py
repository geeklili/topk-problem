def bubble_sort(li):
	"""
	选择排序，选最大值
	:param li:数组
	"""
	# 倒序遍历数组的index
	for ind in range(len(li))[::-1]:
		# 令本次数组的最大值的index为0
		# 去出数组的前ind+1个，即i的取值为0-ind
		for i in range(ind):
			# 如果大于，则与相邻的交换
			if li[i] > li[i + 1]:
				li[i], li[i + 1] = li[i + 1], li[i]


if __name__ == '__main__':
	li = [5, 2, 9, 10, 7, 3, 1]
	bubble_sort(li)
	print(li)
