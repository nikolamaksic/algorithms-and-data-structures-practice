import unittest
from .RemoveDigitFromNumbertoMaximizeResult import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_regular_case(self):
        self.assertEqual(self.solution.removeDigit("123", "3"), "12")
        self.assertEqual(self.solution.removeDigit("1231","1" ), "231")

    def test_more_digits_in_number(self):
        self.assertEqual(self.solution.removeDigit("551","5"), "51")
        self.assertEqual(self.solution.removeDigit("123547956571","5"), "12354796571")

    def test_string_without_digit(self):
        self.assertEqual(self.solution.removeDigit("1234","5"), "1234")
    
    def test_string_starting_with_digit(self):
        self.assertEqual(self.solution.removeDigit("743","7"), "43")


if __name__ == '__main__':
    unittest.main()