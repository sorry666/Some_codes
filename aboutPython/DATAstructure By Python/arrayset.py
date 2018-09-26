"""
File:arrayset.py
Date:Sep-26 2018

"""


from arraybag import ArrayBag 
from abstractset import AbstractSet 




class ArrsySet(ArrayBag,AbstractSet):
	"""An array-based implementation of a set"""



	def __init__(self,sourceCollection = None):
		ArrayBag.__init__(self,sourceCollection)


	def add(self,item ):
		"""Add item to the set if it is not in the set """
		if not item in self:
			ArrayBag.add(self,item)



			