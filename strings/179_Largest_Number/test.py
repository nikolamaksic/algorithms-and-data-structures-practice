import unittest
from .LargestNumber import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_largest_num(self):
        self.assertEqual(self.solution.largestNumber([3,30,34,5,9]), "9534330")
        self.assertEqual(self.solution.largestNumber([10,2]), "210")

if __name__ == '__main__':
    unittest.main()