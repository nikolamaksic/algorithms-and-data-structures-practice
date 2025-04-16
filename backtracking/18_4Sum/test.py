import unittest
from .FourSum import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_standard_case(self):
        result = self.solution.fourSum([1,0,-1,0,-2,2], 0)
        expected = [[-2,-1,1,2],[-1,0,0,1],[-2,0,0,2]]
        self.assertEqual(result, expected)

    def test_all_same_numbers(self):
        result = self.solution.fourSum([2,2,2,2,2], 8)
        expected = [[2,2,2,2]]
        self.assertEqual(result, expected)

    def test_performance(self):
        result = self.solution.fourSum([-489,-475,-469,-468,
        -467,-462,-456,-443,-439,-425,-425,-410,-401,-342,
        -341,-331,-323,-307,-299,-262,-254,-245,-244,-238,
        -229,-227,-225,-224,-221,-197,-173,-171,-160,-142,
        -142,-136,-134,-125,-114,-100,-86,-81,-66,-47,-37,
        -34,4,7,11,34,60,76,99,104,113,117,124,139,141,143,
        144,146,157,157,178,183,185,189,192,194,221,223,226,
        232,247,249,274,281,284,293,298,319,327,338,340,
        368,375,377,379,388,390,392,446,469,480,490], 2738)
        expected = []
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()