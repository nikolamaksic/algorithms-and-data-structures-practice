import unittest
from TwoSumSolution import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])
        self.assertEqual(self.solution.twoSum([2, 5, 5, 11], 10), [1, 2])

    def test_no_solution(self):
        self.assertEqual(self.solution.twoSum([1, 2, 3], 7), -1)

    def test_empty_list(self):
        self.assertEqual(self.solution.twoSum([], 1), -1)

    def test_single_element(self):
        self.assertEqual(self.solution.twoSum([1], 2), -1)

if __name__ == '__main__':
    unittest.main()