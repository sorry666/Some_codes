"""

File:arrays.py
Data:2018-08-27
数据结构Python语言描述P70
"""
class Array(object):
	"""Represents an array"""
	def __init__(self,capacity,fillValue=None):
		"""Capacity is the static size of the array .
		fillValue  is place at each position """
		self._items = list()
		for count in range(capacity):
			self._items.append(fillValue)


	def __len__(self):
		"""-> The capacity of the array"""
		return len(self._items)

	def __str__(self):
		"""The string representation of the array"""
		return	str(self._items)


	def __iter__(self):
		"""Support traversal with a for loop"""
		return iter(self._items)



	def __getitem__(self,index):
		"""Subcript operator for access at index"""
		return self._items[index]



	def __setitem__(self,item,newItem):
		"""Subcript operator for replacement at index"""
		self._items[index] = newItem




		

