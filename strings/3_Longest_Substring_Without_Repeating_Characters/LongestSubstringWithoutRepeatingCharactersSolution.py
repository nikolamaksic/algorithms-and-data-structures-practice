class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        maxSubsLen = 0
        l = 0
        r = 0
        currentCharPos = {}
        while r<len(s):
            if s[r] in currentCharPos and currentCharPos[s[r]] >= l:
                l = currentCharPos[s[r]]+1
            
            maxSubsLen = max(maxSubsLen, r-l+1)
            currentCharPos[s[r]] = r
            r+=1
        return maxSubsLen
