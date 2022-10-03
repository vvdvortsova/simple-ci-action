import unittest
from datetime import datetime 

from system_under_test import *

class TestMyMath(unittest.TestCase):
  def setUp(self):
    self.tick = datetime.now()

  def tearDown(self):
    self.tock = datetime.now()
    diff = self.tock - self.tick
    # print((diff.microseconds / 1000), "ms")

  def test_multiplication(self):
    self.assertEqual(MyMath.multiply(3, 4), 12)

  # def test_failure(self):
  #   self.assertEqual(2 + 2, 3)

  def test_fibonacci_slow(self):
    MyMath.fibonacci(30)

if __name__ == '__main__':
  unittest.main()
