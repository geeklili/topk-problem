def insert_sort(li):
	"""
	插入排序
	:param li:数组
	"""
	for ind in range(1, len(li)):
		for i in range(ind)[::-1]:
			if li[ind] < li[i]:
				li[ind], li[i] = li[i], li[ind]
				ind = i


if __name__ == '__main__':
	li = [5, 2, 9, 10, 7, 3, 1]
	insert_sort(li)
	print(li)
