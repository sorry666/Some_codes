"""
File:node.py
Date:2018-08-27

"""

class Node(object):
	#REpresents a singly linked node
	

	def __init__(self,data,next=None):
		#Instantiates a Node with a default next of None
		
		self.data=data
		self.next=next

		