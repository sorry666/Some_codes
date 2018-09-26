"""
File: abstractset.py
Date: Sep 26 2018
"""


class AbstractSet(object):
	"""Generic set method implementations """


	#Accessor methods
	def __or__(self,other):
		"""Return the union of the self and other"""
		return self+other



	def __and__(self,other):
		"""Return the intersection of self and other."""
		for item in self:
			if item in other:
				intersection.add(item)
		return intersection
		


	def __sub__(self,other):
		"""Return the difference of self and other."""
		for item in self :
			if not item in other :
				difference.add(item)
		return difference
		

	def issubset(self,other):
		"""Return True if self is a subset of other or False otherwise """
		for item in self :
			if not item in other:
				return False
		return True
		

				

