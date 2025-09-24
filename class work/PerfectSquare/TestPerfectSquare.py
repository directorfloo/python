import unittest
import PerfectSquare
class TestCaseDivideOrSquareFunction(unittest.TestCase):       
       def test_divide_or_square_exist(self):
		numbers = [2, 3, 4, 9, 6, 25]
		expected = [False, False, True, True, False, True]
		self.assertEqual(get_perfect_square(numbers), expected)
       def test_that_divide_or_square_is_valid(self):
                self.assertRaises(ValueError, PerfectSquare.get_divide_or_square, [4, 9.5, 16])
       def test_that_divide_or_square_is_valid2(self):
                self.assertRaises(ValueError, PerfectSquare.get_divide_or_square,[4, -9, 16])
       def test_that_divide_or_square_is_valid3(self):
                self.assertRaises(ValueError, PerfectSquare.get_divide_or_square, [4, "9", 16])
       