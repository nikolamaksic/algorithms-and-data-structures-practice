

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        nums_str = [str(num) for num in nums]
        nums_str.sort(key=lambda x: x*10, reverse=True)
        result = ''.join(nums_str)

        return "0" if result[0] == '0' else result