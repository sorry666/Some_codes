"""

File: Test_listIterator.py
Date: 09-08-2018
Description: 展示列表迭代器listIterator类的用法
"""
from arraylist import Arraylist

print("Creat a list with 1-9")
lyst = Arraylist(range(9))
print("length:",len(lyst))
print("Items (first to last ):",lyst)

# Creat and use a list Iterator
listIterator = lyst.listIterator()

print("Forward traversal: ",end = " ")
listIterator.first()
while listIterator.hasNext():
	print(listIterator.next(),end = " ")

print("\n Backward traveal: ",end =" ")
listIterator.last()
while listIterator.hasPrevious():
	print(listIterator.Previous(),end= " ")

print("\nInterting 10 before 3: ",end = " ")
listIterator.first()
for count in range(2):
	listIterator.next()

listIterator.insert(10)
print(lyst)

print("Remove 2:",end = " ")
listIterator.first()
for count in range(3):
	listIterator.next()
listIterator.remove()
print(lyst)


print("Removing all items ")
listIterator.first
while listIterator.hasNext():
	listIterator.next()
	listIterator.remove()
print("Length: ",len(lyst))	




