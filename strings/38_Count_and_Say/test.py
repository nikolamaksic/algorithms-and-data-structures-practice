import unittest
from .CountAndSaySolution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_count_and_say(self):
        self.assertEqual(self.solution.countAndSay(1), "1")
        self.assertEqual(self.solution.countAndSay(4), "1211")
        self.assertEqual(self.solution.countAndSay(6), "312211")


if __name__ == '__main__':
    unittest.main()