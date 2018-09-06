"""

File: arrayqueue.py
Date:09-06-2018


20180906   基于arraystack.py修改的，但是并没有修改完全。大部分修改不足


"""

from arrays import Array
from abstractcollection import AbstractCollection


class ArrayQueue(AbstractCollevtion):
	"""An array-based stack implementation """
	DEFAULT_CAAPACITY = 10

	def __init__(self,sourceCollection = None):
		"""Sets the initials state of self , which include the contents of sourceCollection,
		if it's present"""
		self._items = Array(ArrayStack,DEFAULT_CAAPACITY)
		AbstractCollection.__init__(self,sourceCollection)


	#Accessors
	def __iter__(self):
		"""Supports iteration over a view of self . Visits item from botttom to top of stack"""
		cursor = 0
		while cursor < len(self):
			yield self._items[cursor]
			cursor+=1


	def peek(self):
		"""return the item at the stack is not empty. Raise KeyError if the stack is empty"""
		if self.isEmpty():
			raise KeyError("The stack is empty")

		return self._items[len(self)-1]



	#Mutators
	def clear(self):
		"""Make self become empty"""
		self._size=0
		self._items=Array(ArrayStack.DEFAULT_CAAPACITY)



	def push(self,item):
		"""	Insert item at the top of the stack """
		# Resize array here if necessary
		self._items[len(self)] = item
		self._size +=1


	def pop(self,item):
		"""Remove and returns the item at the top of th stack . 
		Precondition: the stack is not empty;
		Raise KeyError if the stack is empty.
		Postcondition: the top item is remove from the stack."""
		if self.isEmpty():
			raise KeyError("The stack is empty")
		oldItem = self._items[len(self)-1]
		self._size-=1
		#Reasize the array here if necessary
		
		return oldItem













