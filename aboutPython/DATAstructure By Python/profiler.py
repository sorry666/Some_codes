"""
File: profiler.py

Defines a class for profiling sort algorhms.
A profiler object tracks the list , the number of comparisons
and exchanges, and the running time . The Profiler can also 
print a trace and can create a list of unique or duplicate numbers.


Examples use :

from profiler import Profiler
from algorithms import selectionSort

p=Profiler()
p.test(selectionSort,size=15,comp=True,exch=True,trace=True)

"""
import time
import random


class Profiler(object):
	def test(self,function,lyst=None,size=10,unique=True,comp=True,exch=True,trace=False):
		"""
		function: the algorithm being profiled
		target: the search target if profiling a search 
		lyst:allow the caller to use her list
		size: the size of the list ,10 by default
		unique: if True,list contain unique integers
		comp:if true ,count comparisons
		exch:if True,count exchange
		trace:if True ,print the list after each exchange

		Run the function with given attributes and print its profile results.
		"""
		self._comp=comp
		self._exch=exch
		self._trace=trace
		if lyst != None:
			self._lyst=lyst
		elif unique:
			self._lyst=list(range(1,size+1))   #####未加list前报错，说类型不符合，增加list后问题已经解决
			random.shuffle(self._lyst)
		else:
			self._lyst=[]
			for count in range(size):
				self._lyst.append(random.randint(1,size))
		self._exchCount=0
		self._compCount=0
		self._startClock()
		function(self._lyst,self)
		self._stopClock()
		print(self)


	def exchange(self):
		""""Count exchanges if on"""
		if self._exch:
			self._exchCount+=1
		if self._trace:
			print(self._lyst)


	def comparison(self):
		"""Counts comparisons if on"""
		if self._comp:
			self._compCount+=1


	def _startClock(self):
		"""Record the starting time """
		self._start=time.time()


	def _stopClock(self):
		"""Stop the clock and computes the elapsed time in seconds,to the nearest millisecond"""
		self._elapsedTime=round(time.time()-self._start,3)


	def __str__(self):
		"""Return the results as  a string """
		result ="Problem size: "
		result+=str(len(self._lyst))+"\n"
		result+="Elapsed time: "
		result +=str(self._elapsedTime)+"\n"
		if self._comp:
			result+="Comparisons: "
			result+=str(self._compCount)+"\n"
		if self._exch:
			result+="Exchange: "
			result+=str(self._exchCount)+"\n"
		return result
			
