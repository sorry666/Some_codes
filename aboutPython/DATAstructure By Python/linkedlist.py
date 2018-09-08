"""
File:linkedlist.py
Date:09-08-2018 20:08

"""

from node import Node 
from abstractlist import AbstractList


class LinkedList(AbstractList):
	"""A link-based list implementation"""


	def __init__(self,sourceCollection = None):
		"""Set the inital state  of self,which include the contents 
		of soureCollection ,if it's present """
		# Use a circular structure with a sential node 
		self._head = TwoWayNode()
		self._head.previou = self._head.next = self._head
		AbstractList.__init__(self,sourceCollection)


	def __iter__(self):
		"""Support iteration over a view of self """
		cursor = self._head.next
		while cursor != self._head:
			yield cursor.data
			cursor = cursor.next


	# Helper method return node at position 
	def _getNode(self,i):
		"""Helper methods: return a pointer to the node at position i """
		if  i== len(self):
			return self._head
		if i == len(self)-1:
			return self._head.previous
		probe =self._head.next
		while i >0:
			probe = probe.next
			i -=1
			return probe




	# Mutator methods 		

	def __setitem__(self,i,item):
		"""Precondition: 0<=i<len(self)
		Replace the item at position i
		Raise IndexError"""
		if i <0 or i >=len(self):
			raise IndexError("List index out of range ")
		self._getNode(i).data = item
		


	def insert(self,i,item):
		"""Inserts the item at position i """
		if i <0:
			i = 0
		elif i > len(self):
			i= len(self)
		theNode = TwoWayNode(item,theNode.previous,theNode)
		theNode.previous.next = newNode
		self._size +=1
		self.inModCount()


			





	def pop(self):
		pass










