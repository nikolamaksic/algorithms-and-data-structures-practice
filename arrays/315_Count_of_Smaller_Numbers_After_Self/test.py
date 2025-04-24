import unittest
from .CountSmaller import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_count_smaller(self):
        self.assertEqual(self.solution.countSmaller([5,2,6,1]), [2,1,1,0])


if __name__ == '__main__':
    unittest.main()