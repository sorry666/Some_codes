"""
File:profiler1.py
Date:Sep-27  2018
Description:
数据结构p258的例程，
与前文的类不同。
"""
from hashtable import HashTable

class Profiler(object):
	""" Represent a profiler for hash table"""

	def __init__(self):
		self._table = None
		self._collisions = 0
		self._probeCount = 0



	def test(self,table,data):
		"""返回带有给定的数据集的一个表上探查器"""
		self._table = table
		self._collisions = 0
		self._probeCount = 0

		self._result = "Load Factor Item Insert " + "Home Index Actual Index Probes "
		for item in data :
			loadFactor = table.loadFactor()
			table.insert(item)
			homeIndex = table.homeIndex
			actualIndex = table.actualIndex()
			probes = table.probeCount()
			self._probeCount +=probes
			if probes > 0 :
				self._collisions +=1
			line = "%8.3f%14d%12d%12d%14d"%(loadFactor,item,homeIndex,actualIndex,probes)
			self._result += line + "\n" 
			self._result += "Total collision :"+ str(self._collisions)+ "\nTotal probes:"+\
				str(self._probecount)+"\n Average probe per collision :"+str(self._probeCount/self._collisions)

			






	def __str__(self):
		"""返回结果的格式化的表格"""
		if self._table is None :
			return "None test has been run yet "
		else:
			return self._result
			



	def collisions(self):
		"""返回冲突的总次数"""
		pass



	def probeCount(self):
		"""返回解决冲突所需要的总的探查次数"""
		pass


