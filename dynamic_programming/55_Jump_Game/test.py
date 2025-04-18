import unittest
from .JumpGame import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longest_substring(self):
        self.assertEqual(self.solution.canJump([2,3,1,1,4]), True)
        self.assertEqual(self.solution.canJump([3,2,1,0,4]), False)
        self.assertEqual(self.solution.canJump([1,2,3]), True)


if __name__ == '__main__':
    unittest.main()