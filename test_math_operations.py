import unittest
import math_operations

class Tests(unittest.TestCase):

    def test_add(self):
        self.assertEqual(math_operations.add(6,6),12)
        self.assertEqual(math_operations.add(-1,2),1)
        self.assertEqual(math_operations.add(-5,2),-3)

    def test_multiply(self):
        self.assertEqual(math_operations.multiply(6,3),18)
        self.assertEqual(math_operations.multiply(1,1),1)
        self.assertEqual(math_operations.multiply(5,2),10)

    def test_subtract(self):
        self.assertEqual(math_operations.subtract(6,6),0)
        self.assertEqual(math_operations.subtract(-1,-1),0)
        self.assertEqual(math_operations.subtract(5,2),3)

    def test_divide(self):
        self.assertEqual(math_operations.divide(6,6),1)
        self.assertEqual(math_operations.divide(12,2),6)
        self.assertEqual(math_operations.divide(5,2),2.5)
        self.assertEqual(math_operations.divide(5,0),"Invalid")

if __name__ == "__main__":
    unittest.main()