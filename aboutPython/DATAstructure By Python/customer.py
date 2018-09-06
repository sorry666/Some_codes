"""

File : customer.py
Date : 09-06-2018

"""
import random


class Customer(object):


	@classmethod
	def generateCustomer(cls,probabilityOfNewArrival,arrivalTime,averageTimePerCustomer):
		"""Return a Customer object if the probability of arrival is greater than or equal to 
		a random number, Otherwise ,return None , indicating no new customer"""
		if random.random() <= probabilityOfNewArrival:
			return Customer(arrivalTime,averageTimePerCustomer)

		else:
			return None


		
	def __init__(self,arrivalTime,serviceNeeded):
		self._arrivalTime = arrivalTime
		self._amountOfServiceNeeded = serviceNeeded



	def arrivalTime(self):
		return self._arrivalTime


	def amountOfServiceNeeded(self):
		return self._amountOfServiceNeeded



	def serve(self):
		"""Accept a unit of service from the cashier"""

		self._amountOfServiceNeeded -=1



			