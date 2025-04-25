import unittest
from .NumberOfProvinces import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_number_of_provinces(self):
        self.assertEqual(self.solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]), 2)
        self.assertEqual(self.solution.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]), 3)


if __name__ == '__main__':
    unittest.main()