class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ret_str = []
        def backtrack(currStr, open_count, close_count):
            if open_count==n and close_count==n:
                ret_str.append(currStr)
                return
            if open_count<n:
                backtrack(currStr+"(", open_count+1, close_count)
            if close_count<n and open_count>close_count:
                backtrack(currStr+")", open_count, close_count+1)
        backtrack("", 0, 0)

        return ret_str
            
        