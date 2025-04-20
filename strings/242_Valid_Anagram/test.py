import unittest
from .ValidAnagram import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_anagrams_case(self):
        self.assertEqual(self.solution.isAnagram("anagram","nagaram"), True)

    def test_nonanagrams_case(self):
        self.assertEqual(self.solution.isAnagram("rat","car"), False)

if __name__ == '__main__':
    unittest.main()