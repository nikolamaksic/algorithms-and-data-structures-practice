import unittest
from .HIndex import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_h_index(self):
        self.assertEqual(self.solution.hIndex([3,0,6,1,5]), 3)
        self.assertEqual(self.solution.hIndex([1,3,1]), 1)
        self.assertEqual(self.solution.hIndex([4,0,6,1,5]), 3)
        self.assertEqual(self.solution.hIndex([0,0,2]), 1)


if __name__ == '__main__':
    unittest.main()