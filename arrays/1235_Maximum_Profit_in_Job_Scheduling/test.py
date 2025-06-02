import unittest
from .MaximumProfitinJobScheduling import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_profit(self):
        self.assertEqual(self.solution.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]), 120)


if __name__ == '__main__':
    unittest.main()