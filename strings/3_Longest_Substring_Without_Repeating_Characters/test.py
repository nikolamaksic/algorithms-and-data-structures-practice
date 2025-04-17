import unittest
from .LongestSubstringWithoutRepeatingCharactersSolution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longest_substring(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

    def test_longest_substring_empty_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_longest_substring_single_char_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("b"), 1)

if __name__ == '__main__':
    unittest.main()