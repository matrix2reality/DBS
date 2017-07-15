### Python calculator: 
### lambda, map, reduce, list comprehension methods
### Nicolenco Svetlana
### 10265376

import math

class calculator(object):

	# Use reduce method to add numbers within one list - x
	def add(self, x, y):
		result = lambda x,y: x+y
		return reduce(result, x)

	#Use map and lambda method to do calculations for two lists.
	def sum(self, x, y):
		result = lambda x,y: x+y
		return map(result, x,y)
	
	def subtraction(self, x, y):
		result = lambda x,y: x-y	
		return map(result, x,y)

	def multiplication(self, x, y):
		result = lambda x,y: x*y
		return map(result, x,y)

	# zero error handling 
	def division(self, x, y):
		error_check = "False"
		for i in y:
			if i == 0:
				error_check = "True"
		if error_check != "True":
			return map(lambda a,b:a/b, x,y)
		else:
			return "Error - Division to zero"
			
	def sqroot(self, x):
		return [round(math.sqrt(i),2) for i in x]	

	def cube(self, x):
		result = lambda a : a**3
		return map(result, x)

	def log10(self, x):
		result = lambda x: round(math.log10(x), 2)
		return map(result, x)

	def exponent(self, x, y):
		result = lambda x: round(math.exp(x), 2)
		return map(result, x)
		
	def sin(self, x):
		result = lambda x: round(math.sin(float(x)*3.1416/180),2)
		return map(result, x)
	
x=[1,3,70,16]
y=[6,9,0,25]

c = calculator()		

print 'adding numbers within one list = ', c.add(x,y)
print 'sum of numbers of lists x and y = ', c.sum(x, y)
print 'substraction of numbers of lists x and y = ', c.subtraction(x, y)
print 'multiplication of numbers of lists x and y = ', c.multiplication(x, y)
print 'division of numbers of lists x and y = ', c.division(x, y)
print "list comprehension method for square root is ", c.sqroot(x)
print 'Cube of numbers in x is: ', c.cube(x)
print 'log10 of numbers in x is: ', c.log10(x)
print 'exponent of numbers in x is: ', c.exponent(x, y)
print 'sin of numbers in x is: ', c.sin(x)	
	

