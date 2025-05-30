import unittest
from .FirstMissingPositive import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_first_missing_positive(self):
        self.assertEqual(self.solution.firstMissingPositive([1,2,0]), 3)
        self.assertEqual(self.solution.firstMissingPositive([3,4,-1,1]), 2)
        self.assertEqual(self.solution.firstMissingPositive([7,8,9,11,12]), 1)


if __name__ == '__main__':
    unittest.main()