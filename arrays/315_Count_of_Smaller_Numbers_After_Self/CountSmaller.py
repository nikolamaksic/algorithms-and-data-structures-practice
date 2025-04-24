class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        row = [0 for _ in range(n)]
        total = [0 for _ in range(n)]
        for i in range(n):
            row = [0 for _ in range(n)]
            for j in range(i, n):
                row[j] = 1 if nums[i]>nums[j] else 0
            total[i] = sum(row)
        return total