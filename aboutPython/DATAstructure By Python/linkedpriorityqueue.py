"""
File: linkedpriorityqueue.py
Date: 09-06-2018

"""

from node import Node 
from linkedqueue import LinkedQueue 

class LinkedPriorityQueue(LinkedQueue):
	"""A linked-based priority queue implementation"""

	def __init__(self,soureCollection = None):
		"""Set the initial state of self, which includes the contents of soureCollection,if it's
		present"""
		LinkedQueue.__init__(self,soureCollection)


	def add(self,newItem):
		"""Insert newItem after items of greater or equal priority or ahead of item of lesser 
		priority A has greater priority than B if A <B"""
		if self.isEmpty() or newItem >= self._rear.data:
			# New item goes at rear 
			LinkedQueue.add(self,newItem)
		else:
			# Search for a position where it's less
			probe = self._front
			while newItem >= probe.data:
				trailer = probe
				probe = probe.next
			newNode = Node(newItem,probe)
			if probe == self._front:
				#new item does at front
				self._front = newNode
			else:
				# New item goes between two nodes
				trailer.next = newNode
			self._size +=1
				




