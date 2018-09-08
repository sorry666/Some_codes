"""
File:arraylist.py
Date:09-08-2018

"""


from arrays import Array 
from abstractlist import AbstractList 
from arraylistiterator import ArrayListIterator 


class ArrayList(AbstractList):
	"""An arrray-based list implementation."""
	DEFAULT_CAPACITY = 10



	def __init__(self,sourceCollection = None):
		"""Set the initial state of self ,which includes the contnents of sourceCollection ,if it's
		present"""
		self._items = Array(ArrayList.DEFAULT_CAPACITY)
		AbstractList.__init__(self,sourceCollection)



	# Accessor methonds
	def __iter__(self):
		"""Support iteration over a view of self."""
		cursor = 0
		while cursor < len(self):
			yield self._items[cursor]
			cursor +=1


	def  __getItem__(self,i):
		"""Precondition: 0<=i <len(self)
		Return the item at position i.
		Raise IndexError.
		"""	
		if i <0 or i >= len(self):
			raise IndexError("List index out of range")
		return self._items[i]
		


	# Mutator methods
	def __setitem__(self,i,item):
		"""Precondition: 0<=i <len(self)
		Return the item at position i.
		Raise IndexError.
		"""	
		if i <0 or i >= len(self):
			raise IndexError("List index out of range")
		self._items[i] = item


	def insert(self,i,item):
		"""Insert the item at position i."""
		# Resize array here if necessary 
		if i <0:
			i = 0
		elif i > len(self):
			i = len(self)
		if i <len(self):
			for j in range(len(self),i,-1):
				self._items[j] = self._items[j-1]

		self._items[i] = item
		self._size +=1
		self.inModCount()



	def pop(self,i = None):
		"""Precondition 0<=i<len(self).
		Remove and return the item at position i
		If i is None , i is given a default of len(self)-1
		Raise:IndexError"""
		if i ==None:
			i = len(self)-1
		if i <0 or i >= len(self):
			raise IndexError("list index out of range ")
		item = self._items[i]
		for j in range(i,len(self)-1):
			self._items[j] = self._items[j+1]
		self._size -=1
		self.inModCount()
		#Resize array here if necessary
		return item




	def listIterator(self):
		"""Return a list iterator """
		return ArrayListIterator(self)





