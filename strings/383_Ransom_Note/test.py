import unittest
from .RansomNote import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_cannt_construct(self):
        self.assertEqual(self.solution.canConstruct("a","b"), False)
        self.assertEqual(self.solution.canConstruct("aa","ab"), False)
    
    def test_can_construct(self):
        self.assertEqual(self.solution.canConstruct("aa", "aab"), True)


if __name__ == '__main__':
    unittest.main()