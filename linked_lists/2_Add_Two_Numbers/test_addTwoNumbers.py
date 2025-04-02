import unittest
from .AddTwoNumbersSolution import Solution
from ..utils import ListNode, LinkedList

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_numbers(self):
        arg1 = LinkedList([2,4,3])()
        arg2 = LinkedList([5,6,4])()
        res1 = LinkedList([7,0,8])()
        self.assertEqual(self.solution.addTwoNumbers(arg1, arg2), res1)

    def test_adding_two_zeros(self):
        arg1 = LinkedList([0])()
        arg2 = LinkedList([0])()
        res1 = LinkedList([0])()
        self.assertEqual(self.solution.addTwoNumbers(arg1, arg2), res1)
        
    def test_adding_two_numbers_with_different_number_of_digits(self):
        arg1 = LinkedList([9,9,9,9,9,9,9])()
        arg2 = LinkedList([9,9,9,9])()
        res1 = LinkedList([8,9,9,9,0,0,0,1])()
        self.assertEqual(self.solution.addTwoNumbers(arg1, arg2), res1)



if __name__ == '__main__':
    unittest.main()