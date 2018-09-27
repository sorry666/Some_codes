"""
File:hashtable.py
Date:Sep-27 2018
Case study in chapter 11
Description:缺少部分方法的实现，需要补充
"""


from arrays import Array 



class HashTable(object):
	"""Represents a hash table"""


	EMPTY = None
	DELETED = True


	def __init__(self,capacity= 29,hashFunction = hash,linear = True):
		self._table = Array(capacity,HashTable.EMPTY)
		self._size = 0
		self._hash = hashFunction
		self._homeIndex = -1
		self._actualIndex = -1
		self._linear = linear
		self._probecount = 0


	def insert(self,item):
		"""将item插入表中，先决条件：至少有一个空方"""
		pass




	def __len__(self):
		"""返回表中的项数"""
		pass



	def loadFactor(self):
		"""返回表的当前装载因子，项数除以容量"""
		pass



	def homeIndex(self):
		"""返回最近插入、删除或访问的项的主索引"""
		pass




	def actualIndex(self):
		"""返回最近插入、删除或访问的项的主索引"""
		pass



	def probeCount(self):
		"""返回最近插入、删除或访问的项的过程，解决一个冲突的所需的探测次数"""
		pass



	def __str__(self):
		"""和str()相同，返回的表的数组的一个字符串表示，为空的单元格显示值为None
		为之前占用的单元格显示值True
		"""
		pass

		