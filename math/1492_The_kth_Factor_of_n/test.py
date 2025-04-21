import unittest
from KthFactorOfN import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_kth_factor(self):
        self.assertEqual(self.solution.kthFactor(12, 3), 3)
        self.assertEqual(self.solution.kthFactor(7, 2), 7)
        self.assertEqual(self.solution.kthFactor(4, 4), -1)
        self.assertEqual(self.solution.kthFactor(24, 6), 8)


if __name__ == '__main__':
    unittest.main()