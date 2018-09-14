"""
File:arraylist_1.py
Date:Sep 14 2018 20:29
Description:重构后的ArrayList类的代码

"""
from arrays import Array
from abstractlist import AbstractList 
from arraysortedlist import ArraySoredList 
from arraylistiterator import ArrayListIterator


class ArrayList(ArraySoredList):
	"""An array-based list implementation"""


	def __init__(self,soureCollection = None):
		"""Set the initial atate of selt ,which include the cntent of soureCollection 
		if it's present."""
		ArraySoredList.__init__(self,soureCollection)



	# Accessor methods
	def index(self,item):
		"""Precondition: item is in the list.Return the position of the item ,
		Raise: ValueError if the item is not in the list """
		return AbstractList.index(self,item)



	# Mutator methods
	def __setitem__(self,i,item):
		"""Preconditon 0<=i<len(self),
		Replace the item at position i
		Raise: indexError if i is out of the range """
		if i<0 or i>=len(self):
			raise IndexError("List index out of range")
		self._items[i] =item
		

	def insert(self,i,item):
		"""Insert the item at position i"""
		#Resize the array here if necessary
		if i<0:
			i=0
		elif i>len(self):
			i=len(self)
		if i<len(self):
			for j in range(len(self),i,-1):
				self._items[j] = self._items[j-1]

		self._items[i] = item
		self._size +=1
		self.incModCount()


		def add(self,item):
			""" Add item to self."""
			AbstractList.add(self,item)


		def listIterator(self):
			"""return a list iterator """
			return ArrayListIterator(self)



				


