"""
File:abstractcollection.py

目前还没有修改好。20180901


"""


class AbstractCollection(object):

	"""An array-based bag implementation. """

	
	##add some thing 
	#
	

	#Constructor
	#
	def  __init__(self,sourceCollectioon=None):
		"""Sets the initial state of self ,which includes the contents of 
		sourceCollection,if it's present"""

		
		self._size = 0
		if sourceCollectioon:
			for item in sourceCollectioon:
				self.add(item)





	#Accessor methods
	



	

	def __str__(self):
		"""Return the string representation of self"""
		return "{"+",".join(map(str,self))+"}"
		



	def __iter__(self):
		"""Support iteration over a view of self """
		cursor = 0
		while cursor< len(self):
			yield self._items[cursor]
			cursor+=1


	


	def __eq__(self,other):
		"""Return True if self equals other , or False otherwise"""
		if self is other:return True
		if type(self) != type(other) or len(self) !=len(other):
			return False
		otherIter=iter(other)	
		for item in self:
			if not item in other :
				return False
		return True


	def clear(self):
		"""Makes self become empty"""
		self._size = 0
		self._items=Array(ArrayBag.DEFAULT_CAPACITY)



	# def add(self,item):
	# 	"""Add item to self."""
	# 	self._items[len(self)]=item
	# 	self._size+=1


	
	# def remove(self,item):
	# 	"""Precondition : item is in self. Raise: Keyerror if item in not in self.
	# 	postcondition: item is removed from self."""
	# 	#Check precondition and raise if necessary 
	# 	if not item in self:
	# 		raise Keyerror(str(item))+"not a bag"

	# 	#Search for index of target item
	# 	targetIndex = 0
	# 	for targetItem in self:
	# 		if targetItem == item:
	# 			break

	# 	# Shift items to the left of target up by one position 
	# 	for  i in range(targetIndex,len(self)-1):
	# 		self._items[i]=self._items[i+1]

	# 	# Decrement logical size 
	# 	self._size -=1

	# 	# Check arrays memory here and decrease it if necessary
	# 	#  
			

	# 	pass


