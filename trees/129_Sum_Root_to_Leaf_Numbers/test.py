import unittest
from .SumRoottoLeafNumbers import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        self.assertEqual(self.solution.sumNumbers([4,9,0,5,1]), 1026)


if __name__ == '__main__':
    unittest.main()