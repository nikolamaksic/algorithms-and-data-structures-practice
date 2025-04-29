import unittest
from NimGame import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_can_win_nim(self):
        self.assertEqual(self.solution.canWinNim(4), False)
        self.assertEqual(self.solution.canWinNim(5), True)
        self.assertEqual(self.solution.canWinNim(6), True)


if __name__ == '__main__':
    unittest.main()