"""

File: erapp.py
Date: 09-07-2018
Description: The view for an emergence room scheduler

"""

from model1 import ERModel,Patient,Condition


class ERModel(object):
	"""The view class for the ER application."""


	def __init__(self,model):
		self._model = model 

	def run(self):
		"""Menu-drive command loop for app"""
		menu = "Main menu\n"+"1 Schedule a patient \n" + "2 Treat the naxt patient \n"+"3 Treat all patient \n"+"4 Exit the program\n"
		while True:

		    command = self._getCommand(4,menu)
		    if command ==1:
		    	self._schedule()
		    elif command == 2:
		    	self._treatNext()
		    elif command == 3:
		    	self._treatAll
		    else:
		    	break

		    
	def  treatNext(self):
		""" Treat one patient if there is one """
		if self.model.isEmpty():
			print("No patients available to treat ")
		else :
			patient = self.model.treatNext()
			print(patient,"is being treated")




	def treatAll(self):
		"""Treat all the remaining patienting """
		if self.model.isEmpty():
			print("No patients avialiable to be teatd ")
		else:
			while not self.model.isEmpty():
				self.traatNext()


	def _schedule(self):
		"""Obtains patient info and schedules patients"""
		name = input("\n Enter the patients' name : ")
		condition  = self._getCondition()
		self._model.schedule(Patient(name,condition))
		print(name,"is added to the ",condition,"list\n")



	def _getCondition(self):
		"""Obtains conditions info."""
		menu = "Patient's condition :\n"+"1 Critical\n"+"2 Serious\n"+"3 Fair\n"
		number = self._getCommand(3,menu)
		return Condition(number)



	def _getCommand(self):
		"""Obtain and return a command number """
		prompt = "Enter a number [1-" + str(high)+"]:"	
		commandRange = list(map(str,range(1,high + 1)))
		error = "Error, number must be 1 to "+ str(high)
		while True:
			print(menu)
			command = input(prompt)
			if command in commandRange:
				return int(command)
			else:
				print(error)

#main function to start the application 
def main():
	model = ERModel()
	view = ERView(model)
	view.run()

if __name__=="__main__":
	main()







			


