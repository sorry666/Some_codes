"""
File: arraylistiterator.py
Date：Sep 14 2018 16:34

Description:创建一个列表迭代器类
"""


class ArrayListIterator(object):
	"""represents the lists iterator for an array list """




	def __init__(self,backingStore):
		""" Set the initial state of the list iterator"""
		self._backingStore = backingStore
		self._modCount = backingStore.getCount()
		self.first()


	def first(self):
		""" Reset the cursor to the beginning of the backing store"""
		self._cursor = 0
		self._lastItemPos = -1




	def hasNext(self):
		""" Return True if the iterator has a next item or False otherwise"""
		return self._cursor < len(self._backingStore)



	def next(self):
		""" Preconditions: hasNext return True.
		the list has not been modified except by this 
		iterator's mutators.
		Return the current item and advance the cursor to the next item"""
		if not self.hasNext():
			raise ValueError("No next item in the list iterator")
		if self._modCount != self._backingStore.getModCount():
			raise AttributeError("Illegal modification of backing store ")
		self._lastItemPos = self._cursor
		self._cursor +=1
		return self._backingStore[self._lastItemPos]



	def last(self):
		""" Move the cursor to the end of the backing store """
		self._cursor = len(self._backingStore)
		self._lastItemPos =-1




	def hasPrevious(self):
		"""Return True if the iterator has a previous item or False otherwise"""
		return self._cursor >0



	def previous(self):
		"""Precondition:hasPrecondition return True, the list has not modified except 
		by this iterator's mutators.Return the current item and moves the cursor
		 to previous item """
		if not self.hasPrevious():
		 	raise ValueError("No previous item in the list iterator ")
		if self._modCount != self._backingStore.getModCount():
		 	raise AttributeError("Illegal modification of backing store")

		self._cursor -=1
		self._lastItemPos = self._cursor
		return self._backingStore[self._lastItemPos]


	
	def replace(self):
		"""Precondition: the current position is defined .
		the list has not been modified except by this iterator mutators"""
		if self._lastItemPos == -1:
			raise ValueError("The current position is undefined ")
		if self._modCount != self._backingStore.getModCount():
			raise AttributeError("List has been modified illegallly.")
			self._backingStore[self._lastItemPos] = item 
			self._lastItemPos = -1



	def insert(self):
		""" Precondition The list has not been modified except by this iterator mutators."""
		if self._modCount != self._backingStore.getModCount():
			raise AttributeError("List has been modified illgally ")
		if self._lastItemPos == -1:
			#Cursor not defined, so add item to end of list 
			self._backingStore.add(item)
		else:
			self._backingStore.insert(self._lastItemPos,item)
		self._lastItemPos = -1
		self._modCount +=1	



	def remove(self):
		""" Precondition the currnt position is defined .
		The list has not been modified except by this iterator mutators"""
		if self._lastItemPos == -1:
			raise AttributeError("The current position is undefined ")
		if self._modCount != self._backingStore.getModCount():
			raise AttributeError("List has been modified illegally")
		item = self._backingStore.pop(self._lastItemPos)
		
		# If the item removed was obtained via next ,move cursor back
		if self._lastItemPos < self._cursor:
			self._cursor -=1
		self._modCount +=1
		self._lastItemPos = -1



	






