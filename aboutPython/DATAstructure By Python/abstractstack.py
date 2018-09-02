"""

File:abstractstack.py
Date:09-02-2018

"""

from abstractcollection import AbstractCollection 


class AbstractStack(AbstractCollection):
	""" An abstract stack implemenntion """


	# Constructor 
	def __init__(self,sourceCollection=None):
		"""Set the initial state of self, which include the
		contents of sourceCollection ,if it's present"""
		AbstractCollection.__init__(self,sourceCollection)


	# Mutator methods
	def add(self,item):
		"""add items to self """
		self.push(item)