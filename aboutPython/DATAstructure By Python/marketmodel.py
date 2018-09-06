"""
File: marketmodel.py

"""

from cashier import Cashier 
from customer import Customer 


class MarketModel(object):


	def __init__(self,lengthOfSimulation,averageTimePerCus,probabilityOfNewArrival):
		self._probabilitityOfNewArrival = probabilityOfNewArrival
		self._lengthOfSimulation = lengthOfSimulation
		self._averageTimePerCus = averageTimePerCus
		self._cashier = Cashier()




	def runSimulation(self):
		"""Run the clock for n tricks."""
		for currentTime in range(self,_lengthOfSimulation):
			#attempt to genegrate a new customer
			customer = Customer.generateCustomer(self._probabilitityOfNewArrival,currentTime,self._averageTimePerCus)


			# Send customer to cashier if sucessfully generated
			if customer != None:
				self._cashier.addCustomer(customer)

			# Tell cashier to provide another unit of service 
			self._cashier.serveCustomers(currentTime)



	def  __str__(self):
		return str(self._cashier)	

			