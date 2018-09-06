"""

File: comparable.py
Date:09-06-2018

Description: 用于进行比较的类

"""


class Comparable(object):
	""" Wrapper class for items that are not comparable."""


	def __init__(self,data,priority = 1):
		self._data = data
		self._priority = priority 



	def __str__(self):
		"""Return the string rep of the contained datum"""
		return str(self._data)



	def  __eq__(self,other):
		"""Return True if the contained priorities are equal or False otherwise """
		if self is other:
			return True
		if type(self) != type(other):
			return False

		return self._priority == other._priority
		



	def __lt__(self,other):
		"""Return True if self'priority < other'priority,or False otherwise """
		return self._priority < other._priority




	def __le__(self,other):
		"""Return True if self'priority <= other'priority,or False otherwise """
		return self._priority <= self._priority	


	def getData(self):
		"""Return the comtained data"""
		return self._data



	def getPriority(self):
		"""Return the contained priority"""
		return self._priority



		
