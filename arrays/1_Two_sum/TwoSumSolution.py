from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not len(nums):
            return -1
        missingPair = {}
        for i, n in enumerate(nums):
            if target - n in missingPair:
                return [missingPair[target-n], i]
            missingPair[n] = i
        return -1