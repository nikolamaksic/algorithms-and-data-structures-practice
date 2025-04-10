import unittest
from .SearchInsertPosition import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_target_doesnt_exists_in_array(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 2), 1)

    def test_target_exists_in_array(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 5), 2)

    def test_target_lower_than_first_element_in_array(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 0), 0)

    def test_target_greater_than_last_element_in_array(self):
        self.assertEqual(self.solution.searchInsert([1,3,5,6], 7), 4)

if __name__ == '__main__':
    unittest.main()