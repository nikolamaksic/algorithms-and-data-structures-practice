class Solution:
    def canJump(self, nums: list[int]) -> bool:
        N = len(nums)-1
        ret = False
        visited = set()
        def dfs(i):
            visited.add(i)
            if nums[i]+i>=N:
                nonlocal  ret
                ret = True
            else:
                for k in range(i+1,i+nums[i]+1):
                    if not k in visited:
                        dfs(k)
        dfs(0)
        return ret