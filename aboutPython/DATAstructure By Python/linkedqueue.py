"""

File: linkedqueue.py
Date:09-06-2018

20180906 :自行修改作为练习，并未进行校核


"""

from node import Node
from abstractcollection import AbstractCollection 


class LinkedQueue(AbstractCollection):
	"""An linked-based queue implementation """
	

	def __init__(self,sourceCollection = None):
		"""Sets the initials state of self , which include the contents of sourceCollection,
		if it's present"""
		self._items = None
		AbstractCollection.__init__(self,sourceCollection)


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
		Precondition: the squeue is not empty;
		Raise KeyError if the queue is empty.
		."""
		if self.isEmpty():
			raise KeyError("The queue is empty")

		oldItem = self._front.data
		self._front = self._front.next 
		if self._front is None:
			self._rear=None
		self._size -=1
		return oldItem	


	def add(self,newItem):
		"""Adds newItem to the rear of the queue"""
		newNode = Node(newItem,None)
		if self.isEmpty():
			self._front = newNode
		else:
			self._rear.next = newNode
		self._rear = newNode
		self._size +=1
















