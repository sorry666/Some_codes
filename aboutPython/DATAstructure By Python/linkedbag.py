"""
File:linkedbag.py


"""
from node import Node

class LinkedBag(object):

	"""An linked-based bag implementation. """

	# Class varible
	
	#DEFAULT_CAPACITY = 10 

	#Constructor
	#
	def  __init__(self,sourceCollectioon=None):
		"""Sets the initial state of self ,which includes the contents of 
		sourceCollection,if it's present"""

		self._items= None
		self._size = 0
		if sourceCollectioon:
			for item in sourceCollectioon:
				self.add(item)





	#Accessor methods
	def isEmpty(self):
		"""REeturn True if len(self) ==0,or False otherwise"""

		return len(self)==0



	def __len__(self):
		"""Return the numbers of items in self"""

		return self._size

	def __str__(self):
		"""Return the string representation of self"""
		return "{"+",".join(map(str,self))+"}"
		



	def __iter__(self):
		"""Support iteration over a view of self """
		cursor = self._items
		while not cursor is None:
			yield cursor.data
			cursor=cursor.next


	def __add__(self,item):
		"""Return a new bag containing the contents of self and other"""
		result =ArrayBag(self)
		for item in other:
			result.add(item)

		return result


	def __eq__(self,other):
		"""Return True if self equals other , or False otherwise"""
		if self is other:return True
		if type(self) != type(other) or len(self) !=len(other):
			return False
		for item in self:
			if not item in other :
				return False
		return True


	def clear(self):
		"""Makes self become empty"""
		self._size = 0
		self._items=Array(ArrayBag.DEFAULT_CAPACITY)



	def add(self,item):
		"""Add item to self."""
		self._items=Node(item, self._items)
		self._size+=1


	
	def remove(self,item):
		"""Precondition : item is in self. Raise: Keyerror if item in not in self.
		postcondition: item is removed from self."""
		#Check precondition and raise if necessary 
		if not item in self:
			raise Keyerror(str(item))+"not in bag"

		#Search for the node containing of the  target item probe will point to the target 
		#node,and trailer will point to the one before it ,if it exists
		probe=self._items
		trailer=None
		for targetItem in self:
			if targetItem == item:
				break
			trailer= probe
			probe=probe.next

		# Unlock the node to be deleted,either the first one or the one thereafter 
		if probe == self._items:
			self._items=self._items.next
		else:
			trailer.next=probe.next
		
		# Decrement logical size 
		self._size -=1

		# Check arrays memory here and decrease it if necessary
		#  
			

		pass


