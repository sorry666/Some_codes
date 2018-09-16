"""
File:linkedbst.py
Date:Sep 15  2018 10:13
Description:创建一个二叉搜索树，这是AbstractCollection的一个子类
树中的每一个容器，都是类型为BSNode的节点对象，这个节点对象包含了
一个数据段和两个链接字段，这两个连接字段分别名为left和right
这个结构的外部链接名为self._root，在实例化的时候该变量设置为None

"""


from abstractcollection import AbstractCollection 
from bstnode import BSTNode 



class LinkedBST(AbstractCollection):
	""" A link-based binary search tree implemention."""



	def  __init__(self,soureCollection = None):
		"""Set the initial state of the self,which include the 
		content of soureCollection,if it's present"""

		self._root = None 
		AbstractCollection.__init__(soureCollection)



	def find(self,item):
		""" Return data if found or None otherwise."""

		# Helper function to search the binary tree 
		def recurse(node):
			if node is None:
				return None
			elif item == node.data:
				return node.data
			elif item < node.data:
				return recurse(node.left)
			else:
				return recurse(node.right)


		# Top-level call on the root node
		return recurse(self._root)




	def inorder(self):
		"""Support an inorder traversal on a view of self."""
		lyst = list()
		def recurse(node):
			if node != None:
				recurse(node.left)
				lyst.append(node.data)
				recurse(node.right)
		recurse(self._root)
		return iter(lyst)



	def __str__(self):
		""" Return a string representation with the tree rotated
		90 degrees counterclockwise."""


		def recurse(node,level):
			s=""
			if node != Node:
				s +=recurse(node.right,level+1)
				s +="|"*level
				s +=str(node.data)+"\n"
				s +=recurse(node.left,level +1)
			return s
			
		return recurse(self._root,0)
		



	def add(self,item):
		"""ADd item to the tree """


		# Helper function to search for the itrm 's position 
		def recurse(node):
			# New item is less, go left until spot is found
			if item <node.data:
				if node.left == None:
					node.left = BSTNode(item)
				else:
					recurse(node.left)


			# New item is greater or equal; go right until sot is found 
			elif node.right ==None:
				node.right = BSTNode(item)
			else:
				recurse(node.right)

			# End of recurse
			


		# The tree is empty ,so new item goes at the root
		


		if self.isEmpty():
			self._root =BSTNode(item)
		# Otherwise search for the item's spot
		else:
			recurse(self._root)
		self._size +=1
			

				
				
