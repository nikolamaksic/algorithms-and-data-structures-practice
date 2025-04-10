import unittest
from .GenerateParentheses import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_generate_parenthesis(self):
        self.assertEqual(self.solution.generateParenthesis(3), ["((()))","(()())","(())()","()(())","()()()"])

    def test_generate_parenthesis_single_brackets(self):
        self.assertEqual(self.solution.generateParenthesis(1), ["()"])

if __name__ == '__main__':
    unittest.main()