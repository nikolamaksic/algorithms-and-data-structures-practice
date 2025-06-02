import unittest
from .CalculateScoreAfterPerformingInstructions import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_calculate_score(self):
        self.assertEqual(self.solution.calculateScore(["jump","add","add","jump","add","jump"], [2,1,3,1,-2,-3]), 1)
        self.assertEqual(self.solution.calculateScore(["jump","add","add"], [3,1,1]), 0)
        self.assertEqual(self.solution.calculateScore(["jump"], [0]), 0)


if __name__ == '__main__':
    unittest.main()