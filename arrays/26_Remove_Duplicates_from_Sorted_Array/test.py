import unittest
from .RemoveDuplicatesfromSortedArray import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_solution(self):
        testList1 = [1,1,2]
        resultList1 = [1,2]
        self.solution.removeDuplicates(testList1)
        self.assertEqual(testList1, resultList1)
        testList2 = [0,0,1,1,1,2,2,3,3,4]
        resultList2 = [0,1,2,3,4]
        self.solution.removeDuplicates(testList2)
        self.assertEqual(testList2, resultList2)


if __name__ == '__main__':
    unittest.main()