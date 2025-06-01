import unittest
from .DistributeCandiesAmongChildrenII import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        self.assertEqual(self.solution.distributeCandies(5, 2), 3)
        self.assertEqual(self.solution.distributeCandies(3, 3), 10)
        self.assertEqual(self.solution.distributeCandies(14, 12), 111)


if __name__ == '__main__':
    unittest.main()