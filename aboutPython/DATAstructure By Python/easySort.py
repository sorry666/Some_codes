###3.4节 基本排序算法###
#一些简单的排序算法
def swap(lyst,i,j):
	"""Exchange the items at position i and j ."""
	temp=lyst[i]
	lyst[i]=lyst[j]
	lyst[j]=temp



#########	
#选择排序法
############
def selectionSort(lyst):
	i=0
	while i<len(lyst)-1:
		minIndex=i 
		j=i+1
		while j<len(lyst):
			if lyst[j]<lyst[minIndex]:
				minIndex=j
			j+=1
		if minIndex !=i:
			swap(lyst,minIndex,i)
		i+=1



#############
#普通冒泡排序法
##############
def bubbleSort(lyst):
	n=len(lyst)
	while i<n:
		if lyst[i]<lyst[i-1]:
			swap(lyst,i,i-1)
		i+=1
		n-=1





################
#修改的冒泡排序法
#如果在通过主循环时，没有发生交换，那么列表就是已经排序过的了
#这样可以标记起来，当内部出现这样的情况时，直接返回函数。
##############
def bubbleSortWithTweak(lyst):
	n=len(lyst)
	i=1
	while i<n:
		if lyst[i]<lyst[i-1]:
			swap(lyst,i,i-1)
			swapped=true
		if not swapped:return
		n-=1





#####################
#插入排序法
#
def insertionSort(lyst):
	i=1
	while i<len(lyst):
		itemToInsert=lyst[i]
		j=i-1
		while j>=0:
			if itemToInsert<lyst[j]:
				lyst[j+1]=lyst[j]
				j-=1
			else:
				break
		lyst[j+1]=itemToInsert
		i+=1


				