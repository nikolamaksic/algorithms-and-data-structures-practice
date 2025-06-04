import unittest
from .TextJustification import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_text_justification(self):
        self.assertEqual(self.solution.fullJustify(["This", "is", "an", "example", "of", "text", \
            "justification."], 16), ["This    is    an","example  of text","justification.  "])
        self.assertEqual(self.solution.fullJustify(["Science","is","what","we","understand", \
            "well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20),\
                 ["Science  is  what we","understand      well",\
                    "enough to explain to","a  computer.  Art is","everything  else  we","do                  "])


if __name__ == '__main__':
    unittest.main()