"""
File:arraydict.py
Date: Sep-26  2018

"""
from abstractdict import AbstractDict,Item


class ArrayDict(AbstractDict):
	"""Represents an array-based dictinonary"""



	def __init__(self,sourceCollection =None):
		"""Will copy items to the collection from sourceDictionary if it's present."""
		self._items = list()
		AbstractDict.__init__(self,sourceCollection)



	#Accesor
	def __iter__(self):
		"""Serves up the key in th dictinary ."""
		cursor = 0
		while cursor < len(self):
			yield self._items[cursor].key
			cursor +=1


	def __getitem__(self,key):
		"""Precondition: the key is in the dictionary.
		Raise : a keyError if the key is not in the dictionary. Return the value 
		associated with the key ."""
		index = self._index(key)
		if index == -1:
			raise KeyError("Missing:"+str(key))
		return self._items[index].value	



	#Matutors
	def __setitem__(self,key,value):
		"""If the key is not in the dictionary ,add the key and value 
		to it .otherwise .replace the old value with the new value"""
		index = self._index(key)
		if index == -1:
			self._item.append(Entry(key,value))
			self.size +=1
		else:
			self._items[index].value = value


	def pop(self,key):
		"""Precondition:the key is in the dictionary,Raise:a KeyError if the key 
		is not in the dictionary,Remove the key and return the defaults value otherwise 
		"""
		index = self._index(key)
		if index == -1:
			raise KeyError("Missing :"+ str(key))
		self._size -=1
		return self._items.pop(index).value	


	def _index(self,key):
		"""Helper method for key search ."""
		index = 0
		for entry in self._items:
			if entry.key == key:
				return index
			index +=1
		return -1






	
