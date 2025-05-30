import unittest
from .VerticalOrderTraversalofaBinaryTree import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        self.assertEqual(self.solution.sumNumbers([3,9,20, None, None,15,7]), [[9],[3,15],[20],[7]])
        self.assertEqual(self.solution.sumNumbers([1,2,3,4,5,6,7]), [[4],[2],[1,5,6],[3],[7]])
        self.assertEqual(self.solution.sumNumbers([1,2,3,4,6,5,7]), [[4],[2],[1,5,6],[3],[7]])


if __name__ == '__main__':
    unittest.main()