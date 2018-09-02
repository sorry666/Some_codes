"""

File:tokens.py

Tokens for processing expresions

"""

class Token(object):
	UNKNOWN=0   # unknown

	INT = 4    # integer

	MINUS = 5  # minus operator
	PLUS = 6   #plus operator 
	MUL = 7  # multiply operator
	DIV = 8  #divide operator

	FIRST_OP = 5  # first operator 


	def __init__(self,value):
		if type(value) == int:
			self._type =Token.INT
		else:
			self._type==self._makeType(value)
		self._value=value
		


	def isOperator(self):
		return self._type >= Token.FIRST_OP


	def __str__(self):
		return str(self._value)


	def getType(self):
		return self._type


	def getValue(self):
		return self._value


	def _makeType(self,ch):
		if ch=='*':return Token.MUL
		elif ch=='/':return Token.DIV
		elif ch=='+':return Token.PLUS
		elif ch=='-': return Token.UNKNOWN

