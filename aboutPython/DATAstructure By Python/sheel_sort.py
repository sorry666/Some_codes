"""
File: shell_sort.py
Date:Sep 17 2018 21:21
"""

def shell_sort(alist):
	"""希尔排序"""
	n = len(alist)
	gap = n//2
	while gap >0:
		for j in range(gap,n):
			i = j
			while i >0:
				if alist[i]< alist[i-gap]:
					alist[i],alist[i-gap] = alist[i-gap],alist[i]
					i -=gap
				else:
					break



		


	


