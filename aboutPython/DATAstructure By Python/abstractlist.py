"""
File:abatractlist.py
Date:09-08-2018
Description:
建立一个AbstractList类，是AbstractCollection类的一个子类

"""


from abstractcollection import abstractcollection

class AbstractList(AbstractCollection):
	""" An abstract list implemention """


	def __init__(self,sourceCollection):
		"""Maintain a count of modifications to the list """
		self._modCount = 0
		AbstractCollection.__innit__(self,sourceCollection)


	def getModCount(self):
		""" Return the count of modifications to the list """
		return self._modCount



	def inModCount(self):
		"""Incerement the count of modifications to the list"""
		self._modCount +=1



	def index(self,item):
		"""Precondition :item is in the list 
		Return the position of the item 
		Raises: ValueError if the item is not in the list ."""
		position = 0
		for data in self:
			if data == item:
				return position 
			else:
				position +=1
		if position == len(self):
			raise ValueError(str(item) + " not in list ")


	def add(self):
		"""Adds the item to the end of the list """
		self.insert(len(self),item)



	def remove(self,item):
		"""Precondition:item is in self
		Raises: ValueError if item is not in self 
		Postcondition: item is removed from self"""
		position = self.index(item)
		self.pop(position)




		



