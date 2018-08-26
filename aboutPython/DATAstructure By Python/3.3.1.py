###最小项搜索
def indexOfMin(lyst):
	"""Return the index of the minimum item"""
	minIndex =0
	currentIndex=1
	while currentIndex< len(lyst):
		if lyst(currentIndex)<lyst(minIndex):
			minIndex=currentIndex
		currentIndex+=1
	return minIndex



###顺序搜索或线性搜索
def sequentialSearch(target,lyst):
	"""Return the position of the target item if found,or -1 otherwise"""
	position=0
	while position<len(lyst):
		if target==lyst[position]:
			return position
		position+=1
	return -1




###有序列表的二叉树搜索
def binarySearch(target,sortedLyst):
	left=0
	right=len(sortedLyst)-1
	while left<=right:
		midpoint=(left+right)//2
		if target == sortedLyst[midpoint]:
			return midpoint
		elif target<sortedLyst[midpoint]:
			right=midpoint-1
		else:
			left=midpoint+1
	return -1
	



			

