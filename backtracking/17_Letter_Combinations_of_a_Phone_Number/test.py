import unittest
from LetterCombinationOfPhoneNumber import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_standard_case(self):
        result = self.solution.letterCombinations("23")
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(sorted(result), sorted(expected))

    def test_empty_input(self):
        result = self.solution.letterCombinations("")
        self.assertEqual(result, [])

    def test_single_digit(self):
        result = self.solution.letterCombinations("2")
        expected = ["a", "b", "c"]
        self.assertEqual(sorted(result), sorted(expected))

    def test_multiple_digits(self):
        result = self.solution.letterCombinations("79")
        expected = ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]
        self.assertEqual(sorted(result), sorted(expected))

    def test_longer_sequence(self):
        result = self.solution.letterCombinations("234")
        expected = [
            "adg", "adh", "adi", "aeg", "aeh", "aei", "afg", "afh", "afi",
            "bdg", "bdh", "bdi", "beg", "beh", "bei", "bfg", "bfh", "bfi",
            "cdg", "cdh", "cdi", "ceg", "ceh", "cei", "cfg", "cfh", "cfi"
        ]
        self.assertEqual(sorted(result), sorted(expected))

if __name__ == '__main__':
    unittest.main()