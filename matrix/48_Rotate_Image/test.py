import unittest
from .RotateImage import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rotate_image(self):
        mat = [[1,2,3],[4,5,6],[7,8,9]]
        self.solution.rotate(mat)
        self.assertEqual(mat, [[7,4,1],[8,5,2],[9,6,3]])


if __name__ == '__main__':
    unittest.main()