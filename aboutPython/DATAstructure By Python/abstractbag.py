"""
File:abstractbag.py


"""


class AbstractBag(object):

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
		cursor = 0
		while cursor< len(self):
			yield self._items[cursor]
			cursor+=1


	def __add__(self,other):
		"""Return a new bag containing the contents of self and other"""
		result =type(self)(self)
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


