from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = set()
        nums.sort()

        def dfs(index, currSum, currMembr):
            if len(currMembr) == 4:
                if currSum == target:
                    ret.add(tuple(currMembr))
                return
            if index >= len(nums):
                return
            dfs(index + 1, currSum, currMembr)
            dfs(index + 1, currSum + nums[index], currMembr + [nums[index]])

        dfs(0, 0, [])
        return [list(t) for t in ret]
