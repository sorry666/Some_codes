"""

File: linkedstack.py
Date:09-02-2018



2018092:还需要修改peek()和pop()方法的先验条件，强制引发异常.

"""

from node import Node
from abstractstack import AbstractStack 


class LinkedStack(AbstractStack):
	"""An linked-based stack implementation """
	

	def __init__(self,sourceCollection = None):
		"""Sets the initials state of self , which include the contents of sourceCollection,
		if it's present"""
		self._items = None
		AbstractStack.__init__(self,sourceCollection)


	#Accessors
	def __iter__(self):
		"""Supports iteration over a view of self . Visits item from botttom to top of stack"""
		def visitNodes(node):
			if not node is Node:
				visitNodes(node.next)
				tempList.append(node.data)
		tempList = list()
		visitNodes(self._items)
		return iter(tempList)		
	

	def peek(self):
		"""return the item at the stack is not empty. Raise KeyError if the stack is empty"""
		if self.isEmpty():
			raise KeyError("The stack is empty")
		return self._items[len(self)-1]



	#Mutators
	def clear(self):
		"""Make self become empty"""
		self._size=0
		self._items=None



	def push(self,item):
		"""	Insert item at the top of the stack """
		# Resize array here if necessary
		self._items=Node(item,self._items)
		self._size +=1


	def pop(self,item):
		"""Remove and returns the item at the top of th stack . 
		Precondition: the stack is not empty;
		Raise KeyError if the stack is empty.
		Postcondition: the top item is remove from the stack."""
		if self.isEmpty():
			raise KeyError("The stack is empty")

		oldItem = self._items.data
		self._items=self._items.next
		self._size-=1
		#Reasize the linked here if necessary
		
		return oldItem













