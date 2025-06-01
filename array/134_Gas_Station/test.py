import unittest
from .GasStation import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_can_complete(self):
        self.assertEqual(self.solution.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]), 3)

    def test_cannt_complete(self):
        self.assertEqual(self.solution.canCompleteCircuit([2,3,4], [3,4,4]), -1)


if __name__ == '__main__':
    unittest.main()