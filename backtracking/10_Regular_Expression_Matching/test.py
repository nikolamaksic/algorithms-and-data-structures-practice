import unittest
from .RegularExpressionMatching import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_standard_case(self):
        self.assertEqual(self.solution.isMatch("aaa", "ab*a"), False)
        self.assertEqual(self.solution.isMatch("aa", "a*"), True)
        self.assertEqual(self.solution.isMatch("ab", ".*"), True)
        self.assertEqual(self.solution.isMatch("aa", "a"), False)
        self.assertEqual(self.solution.isMatch("mississippi", "mis*is*p*."), False)
        self.assertEqual(self.solution.isMatch("aaa", "ab*a"), False)


if __name__ == '__main__':
    unittest.main()