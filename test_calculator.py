# https://github.com/Polinadavyyy/lab11--PD---AC-
# Partner 1: Polina Davydouskaya
# Partner 2: Alexander Chasko




import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
        # Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 1), -3)
        self.assertEqual(add(0, 7), 7)

    def test_subtract(self):
        self.assertEqual(subtract(8, 3), 5)
        self.assertEqual(subtract(3, 8), -5)
        self.assertEqual(subtract(4, 4), 0)
    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 5), 10)
        self.assertEqual(mul(-3, 4), -12)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(3, 15), 5)
        self.assertEqual(div(-4, 20), -5)


       # Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(3, 1), 0.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 8)    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(7, -2)
    #

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5)
        self.assertAlmostEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-2)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(0), 0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()