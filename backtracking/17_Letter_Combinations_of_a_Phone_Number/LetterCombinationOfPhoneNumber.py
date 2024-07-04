from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        res = []

        digitsToChar = {
            "2":["a", "b", "c"],
            "3":["d", "e", "f"],
            "4":["g", "h", "i"],
            "5":["j", "k", "l"],
            "6":["m", "n", "o"],
            "7":["p", "q", "r", "s"],
            "8":["t", "u", "v"],
            "9":["w", "x", "y", "z"],
        }

        def dfs(currStr, ind):
            if ind==len(digits):
                res.append(currStr)
                return
            currDigit = digits[ind]
            for ch in digitsToChar[currDigit]:
                dfs(currStr+ch, ind+1)
        dfs("", 0)
        return res