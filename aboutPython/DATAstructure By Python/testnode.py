"""
File:testnode.py
Date:2018-08-27


test the node class

"""

from node import Node



head=None

#Add five nodes to the begining of the linked structure

for count in range(1,6):
	head =Node(count, head)


#Print the contents of the structure
#

while head !=None:
	print(head.data)
	head=head.next

	