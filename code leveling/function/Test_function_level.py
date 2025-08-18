import unittest
import Function_level

class TestCaseAddition(unittest.TestCase):
	def test_addition_exists(self):
		Function_level.get_addition([[4, 6, 8]])

	def test_addition_is_valid(self):
		self.assertRaises(ValueError, Function_level.get_addition, 0)

	def test_addition_is_valid2(self):
		self.assertRaises(ValueError, Function_level.get_addition,"ola")






class TestCaseAddition(unittest.TestCase):
	def test_addition_exists(self):
		Function_level.get_addition([[4, 6, 8]])

	def test_addition_is_valid(self):
		self.assertRaises(ValueError, Function_level.get_addition, 0)

	def test_addition_is_valid2(self):
		self.assertRaises(ValueError, Function_level.get_addition,"ola")


