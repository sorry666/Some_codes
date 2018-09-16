"""

File:expression&parsing10.8.py
Date:Sep 16  2018   15:26
Description:
案例学习：解析和表达式树
设计和实现一个表达式树，以支持处理算数表达式的过程，并且可以径其转化为可替代的其他形式。


"""


class LeafNode(object):
	"""Represents an integer """


	def __init__(self,data):
		self._data = data

	def postfix(self):
		return str(self)

	def __str__(self):
		return str(self._data)




class InteriorNode(object):
	"""Represent an operator and its two operands"""

	def  __init__(self,op,leftOper,rightOper):
		self._operator = op
		self._leftOperand = leftOper
		self._rightOperand = rightOper


	def postfix(self):
		return self._leftOperand.postfix() +" "+\
		self._rightOperand.postfix() + " "+\
		self._operator



	# Syntax rule:
    # factor = number | "("expression")"
    # factor方法负责处理嵌套在圆括号中的数字或表达式。当这个标记是数字的时候，该方法创建
    # 了包含该数字的一个节点并返回它。否则，如果标记的是圆括号，该方法调用expression方法来解析
    # 嵌套的表达式。这个方法返回了表示结果的一个数，且factor将此树传递给其调用者。
    def factor(self):
    	
    	token = self.scanner.get()
    	if token.getType() == Token.INT :
    		tree = LeafNode(token.getValue())
    		self.scanner.next()
    	elif token.getType() == Token.L_PAR:
    		self.scanner.next()
    		tree = self.expression
    		self.accept(self._scanner.get(),Token.R_PAR,"')' expected")
    		self.scanner.next()
    	else:
    		tree = None
    		self.fatalError(Token,"bad factor")
    	return tree
    	

    # Syntax rule 
    # expression = term {addingOperator term }
    # expression方法处理一项，该项后面跟着零个或者多个加法运算符和项。首先调用term方法
    # 它返回表示该项的树。如果当期前的标记的加法运算符，expression只是将树传递给其调用者
    # 否则，expression将会进入一个循环。在这个循环中，expression构建了一个内部节点，其值是
    # 一个加法运算符。其左子树是在最近一次调用term的时候接受的树，其右子树是对term的一次新的调用的接受
    # 的树。当expression没见到加法运算符的时候，这个过程就结束了。
    # Syntax rule:
    # expression = term { addingOperator term }
    def  expression(self):
    	tree = self.term()
    	token = self.scanner.get()
    	while token.getType() in (Token.PLUS,Token.MINUS):
    		op = self.term()
    		self.scanner.next()
    		tree = InteriorNode(op,tree,self.term())
    		token = self.scanner.get()
    	return tree	













		

