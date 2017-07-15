### Python calculator - Test 
### lambda, map, reduce, list comprehension methods
### Nicolenco Svetlana
### 10265376

import unittest

# Import calculation algorithms from the Calculator_List Class in calculator_lists.py

# Set up test data in two lists

x=[1,4,30,16]
y=[-2,6,0,8]

from calculus import calculator

class TestCalculator(unittest.TestCase): 
                 
	def setUp(self):
		self.calc = calculator()

	def test_add(self):
		result = self.calc.add(x,y)
		self.assertEqual(51, result)
		
	def test_sum(self):
		result = self.calc.sum(x,y)
		self.assertEqual([-1,10,30,24], result)
		
	def test_subtraction(self):
		result = self.calc.subtraction(x, y)
		self.assertEqual([3, -2, 30, 8], result)

	def test_multiplication(self):
		result = self.calc.multiplication(x,y)
		self.assertEqual([-2, 24, 0, 128], result)

	def test_sqroot(self):
		result = self.calc.sqroot(x)
		self.assertEqual([1.0, 2, 5.48, 4], result)

	def test_cube(self):
		result = self.calc.cube(x)
		self.assertEqual([1, 64, 27000, 4096], result)

	def test_exponent(self):
		result = self.calc.exponent(x,y)
		self.assertEqual([2.72, 54.6,  10686474581524.46, 8886110.52], result)
		
	def test_log10(self):
		result = self.calc.log10(x)
		self.assertEqual([0, 0.60, 1.48, 1.20], result)

	def test_sin(self):
		result = self.calc.sin(x)
		self.assertEqual([0.02, 0.07, 0.5, 0.28], result)

if __name__ == '__main__':
    unittest.main()