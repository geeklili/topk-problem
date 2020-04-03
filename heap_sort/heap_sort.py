def create_heap(li, ind):
	"""
	构建大顶堆
	:param li: 总数组
	:param n: 构建大顶堆的数组的最大index
	"""
	# 倒序遍历传进来的数组的index
	for pindex in range(ind)[::-1]:
		# 有右节点
		if 2 * pindex + 2 <= ind:
			# 右节点的值大于父节点的值
			if li[2 * pindex + 2] > li[pindex]:
				li[pindex], li[2 * pindex + 2] = li[2 * pindex + 2], li[pindex]
		# 有左节点
		if 2 * pindex + 1 <= ind:
			# 左节点的值大于父节点的值
			if li[2 * pindex + 1] > li[pindex]:
				li[pindex], li[2 * pindex + 1] = li[2 * pindex + 1], li[pindex]


def sort_heap(li):
	"""
	堆排序
	:param li:总数组
	"""
	# 倒序遍历数组的index
	for ind in range(li.__len__())[::-1]:
		# 给该index下的数组构建大顶堆
		create_heap(li, ind)
		# 交换该index下的数组的末尾数据和首位数据
		li[ind], li[0] = li[0], li[ind]


if __name__ == '__main__':
	li = [5, 2, 9, 10, 7, 3, 1]
	sort_heap(li)
	print(li)
