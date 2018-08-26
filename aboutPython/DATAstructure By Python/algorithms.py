"""
File: algorithms.py
Algorithms configured for profiling
"""


def selectionSort(lyst,profiler):
	i=0
	while i< len(lyst)-1:
		minIndex=i
		j=i+1
		while j<len(lyst):
			profiler.comparison()   #count
			if lyst[j]<lyst[minIndex]:
				minIndex=j
			j=j+1
		if minIndex !=i:
			swap(lyst,minIndex,i,profiler)
		i+=1
		


def swap(lyst,i,j,profiler):
	"""Exchange the elements at position i and j """
	profiler.exchange()    #Count
	temp= lyst[i]
	lyst[i]=lyst[j]
	lyst[j]=temp


#testing code can go here ,optionally
				
