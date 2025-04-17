import unittest
from .MinimumConsecutiveCardsToPickUp import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_regular_case(self):
        self.assertEqual(self.solution.minimumCardPickup([3,4,2,3,4,7]), 4)
        self.assertEqual(self.solution.minimumCardPickup([1,0,5,3]), -1)



if __name__ == '__main__':
    unittest.main()