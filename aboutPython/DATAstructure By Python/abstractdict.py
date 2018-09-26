"""
File:abstractdict.py
Date:Sep-26 2018
Description:
包含Item类，和AbstractDict类
"""
from abstractcollection import AbstractCollection 



class AbstractDict(AbstractCollection):
	"""Commmon data and method implementation for dictinary"""
	def __init__(self,sourceCollection):
		"""Will copy items to the collection from sourecollection if it's present"""
		AbstractCollection.__init__(self)
		if sourceCollection:
			for key,value in sourceCollection:
				self[key] = value

	def __str__(self):
		return "{" +",".join(map(str.self.items())) +"}"


	def __add__(self,other):
		"""Return a new dictinary containing the content of self and other"""
		result = type(self)(map(lambda item:(item.key,item.value),self.items() ))
		for key in other:
			result[key] = other[key]
		return result
			


	def __eq__(self,other):
		"""Return True if self equals other,or False otherwise ."""
		if self is other: return True
		if type(self) != type(other) or len(self) != len(other):
			return False
		for key in self:
			if not key in other :
				return False
		return True
		

	def keys(self):
		"""Return a interator on the keys in the dictinary."""
		return iter(self)



	def values(self):
		"""Return an iterator on the values in the dictinary ."""
		return iter(map(lambda key:self[key],self))



	def items(self):
		"""Return an iterator on the item in the dictinary."""
		return iter(map(lambda key :Item(key,self[key]),self))









class Item(object):
	"""Represents a dictinary item , Support comparisons by key"""

	def __init__(self,key,value):
		self.key = key
		self.value = value



	def __str__(self):
		return str(self.key) + ":" + str(self.vaue)


	def __eq__(self,other):
		if type(self) != type(other): return False
		return self.key == other.key


	def __lt__(self,other):
		if type(self)!= type(other) : return False
		return self.key<other.key


	def __le__(self,other):
		if type(self) != type(other): return False
		return self.key <= other.key





