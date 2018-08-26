
from arrays import Array 

def mergeSort(lyst):
	#lyst  list being sorted
	#copyBuffer temporary space needed during merge
	copyBuffer=Array(len(lyst))
	mergeSortHelper=(lyst,copyBuffer,0,len(lyst)-1)

def mergeSortHelper(lyst,copyBuffer,low,hight):
	#lyst list being sorted
	#copyBuffer temp space needed during merge
	#low ,hight  bound of sublist
	#middle  midpint of sublist
	if low<high:
		middle=(low+high//2
		mergeSortHelper(lyst,copyBuffer,low,middle)
		mergeSortHelper(lyst,copyBuffer,middle+1,high)
		merge(lyst,copyBuffer,low,middle,high)

		

def merge(lyst,copyBuffer,low,middle,high)
	#lyst    list that is being sort
	#copyBuffer    temp space needed during the merge process
	#low     beginning of first sorted sublist 
	#middle  end of first sorted sublist 
	#middle+1   beginning of the second sorted sublist
	#high     end of second sorted sublist
	#
	#	
	#		Initialize i1 and i2 to the first item in each sublist
	i1=low
	i2=middle+1
	#Interleave items from the sublists into the copyBuffer in such a way that order is 
	#maintained . 
	
	for i in range(low,high+1):
		if i1>middle:
			copyBuffer[i]=lyst[i2]   #First sublist exhausted
			i2+=1
		elif i2>high:
			copyBuffer[i]=lyst[i1]   #Second sublist exhausted
			i1+=1
		elif lyst[i1]<lyst[i2]:
			copyBuffer[i]=lyst[i1]   #Item in first sublist<
			i1+=1
		else:
			copyBuffer[i]=lyst[i2]  #Item in second sublist
			i2+=1


	for i in range(low ,high+1):
		lyst[i]=Buffer[i]
	    #copy sorted items back to proper position in lyst

