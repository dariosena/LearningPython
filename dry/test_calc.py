import unittest
import calc

class CalcTestCase(unittest.TestCase):
    """Test calc.py"""
    def setUp(self):
        self.num1 = 10
        self.num2 = 5

    def tearDown(self):
        pass

    def test_add(self):
        self.assertTrue(calc.add(self.num1, self.num2), self.num1 + self.num2)

    def test_subtract(self):
        self.assertTrue(calc.subtract(self.num1, self.num2),
                                      self.num1 - self.num2)

    def test_multiply(self):
        self.assertTrue(calc.multiply(self.num1, self.num2),
                                      self.num1 * self.num2)

    def test_divide(self):
        self.assertTrue(calc.divide(self.num1, self.num2),
                                    self.num1 / self.num2)

if __name__ == '__main__':
    unittest.main()
