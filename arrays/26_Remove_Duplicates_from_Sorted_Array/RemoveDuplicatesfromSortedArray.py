class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums)<=1:
            return
        l, r = 0, 1
        while l<len(nums) and r<len(nums):
            if nums[r-1]!=nums[r]:
                l+=1
            nums[l] = nums[r]
            r+=1
        if l<len(nums):
            nums[:] = nums[:l+1]