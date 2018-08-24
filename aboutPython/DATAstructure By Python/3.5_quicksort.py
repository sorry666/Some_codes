
def swap(lyst,i,j):
	"""Exchange the items at position i and j ."""
	temp=lyst[i]
	lyst[i]=lyst[j]
	lyst[j]=temp


def quiccksort(lyst):
	quicksortHelper(lyst,0,len(lyst)-1)



def quicksortHelper(lyst,left,right):
	if left<right:
		pivotLocation=partition(lyst,left,right)
		quicksortHelper(lyst,left,pivotLocation-1)
		quicksortHelper(lyst,pivotLocation+1,right)



def partition(lyst,left,right):
	#find the pivot and exchange it with the last item
	middle=(left+right)//2
	pivot=lyst[right]
	lyst[middle]=lyst[right]
	lyst[right]=pivot
	#Set the boundary point to first position
	boundary=left
	#move items less than pivot to the left 
	for index in range(left,right):
		if lyst[index]<pivot:
			swap(lyst,index,boundary)
			boundary+=1
	#Exchange definition of the swap function goes here
	swap(lyst,right,boundary)
	return boundary





import random 

def main(size=20,sort=quiccksort):
	lyst=[]
	for count in range(size):
		lyst.append(random.randint(1,size+1))
	print(lyst)
	sort(lyst)
	print(lyst)



if __name__=="__main__":
	main()
