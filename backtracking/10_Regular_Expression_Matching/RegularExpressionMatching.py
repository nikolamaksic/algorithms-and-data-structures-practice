class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def backtracking(si, pi):
            if (si, pi) in memo:
                return memo[(si, pi)]
            if pi == len(p):
                return si == len(s)
            first_match = si < len(s) and (p[pi] == s[si] or p[pi] == '.')
            if (pi + 1) < len(p) and p[pi + 1] == '*':
                res = backtracking(si, pi + 2) or (first_match and backtracking(si + 1, pi))
            else:
                res = first_match and backtracking(si + 1, pi + 1)
            memo[(si, pi)] = res
            return res

        return backtracking(0, 0)
