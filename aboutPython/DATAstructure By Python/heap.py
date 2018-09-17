"""

File:heap.py
Date:Sep 17  2018 19:48
Description:
使用heap来实现一个优先队列，堆接口应该包含返回其大小
添加项、删除项、和查看项的方法


备注：该程序并没有完善

"""


class Heap(object):



	def __init__(self,):

		pass



	def isEmpty(self):
		"""如果堆为空，返回True,否则，返回False"""
		pass


	def __len__(self):
		"""返回堆中的项的数目"""
		pass


	def __iter__(self):
		"""从最小到最大地访问各项"""
		pass



	def __str__(self):
		"""返回一个字符串，表示堆的形状"""
		pass



	def __contains__(self,item):
		"""如果item在堆中，返回True，否则返回False。"""
		pass



	def __add__(self,otherHeap):
		"""返回一个新堆，其内容是heap和otherHeap的内容"""
		pass


	def __eq__(self,anyObject):
		"""如果堆等于anyObject的话，返回TRUE，否则返回False。如果两个堆
		包含相同的项，那么他们是相等的"""
		pass


	def peek(self):
		"""返回heap的最顶部的项，先验条件：heap不为空"""
		pass




	def add(self,item):
		"""将item插入到其在heap中适当的位置"""
		self._size +=1
		self._heap.append(item)
		curPos = len(self._heap) - 1
		while curPos > 0 :
			parent = (curPos - 1)//2
			parentItem = self._heap[parent]
			if parentItem <= item:
				break
			else:
				self._heap[curPos] = self._heap[parent]
				self._heap[parent]  = item
				curPos = parent




	def pop(self):
		"""返回heap最顶部的项，先验条件：heap不为空"""
		if self.isEmpty():
			raise Exception,"Heap is empty "
		self._size -=1
		topItem =  self._heap[0]
		bottomItem = self._heap.pop(len(self._heap)-1)
		if len(self._heap) ==0:
			return bottomItem

		self._hap[0] = bottomItem
		lastIndex = len(self._heap) -1
		curPos = 0
		while True:
			leftChild = 2*curPos +1
			rightChild = 2*curPos +2
			if leftChild > lastIndex:
				break
			if rightChild >lastIndex:
				maxChild = leftChild
			else:
				leftItem = self._heap[leftChild]
				rightItem = self._heap[rightChild]
				if leftItem < rightItem:
					maxChild = leftChild
				else:
					maxChild = rightChild
			maxItem = self._heap[maxChild]
			if bottomItem <= maxItem:
				break
			else:
				self._heap[curPos] = self._heap[maxChild]
				self._heap[maxChild] = bottomItem
				curPos = maxChild
		return topItem
		


					






