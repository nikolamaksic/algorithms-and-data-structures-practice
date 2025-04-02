from collections import deque



class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        maxPar = 0
        currentPar = deque()
        currLen = 0


        for ch in s:
            
            if len(currentPar):
                maxPar = max(maxPar, currLen)
            if ch==")":
                if len(currentPar):
                    currentPar.pop()
                    currLen+=2
                else:
                    currLen = 0
            else:
                currentPar.append(ch)
        return maxPar





