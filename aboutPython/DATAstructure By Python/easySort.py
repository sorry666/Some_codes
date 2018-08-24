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
#冒泡排序法
##############
				
