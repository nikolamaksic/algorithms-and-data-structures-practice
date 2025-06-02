class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        starts = [job[0] for job in jobs]
        n = len(jobs)
        mem = {}
        def find_next_index(target):
            left, right = 0, n
            while left < right:
                mid = (left + right) // 2
                if starts[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def dfs(i):
            if i == n:
                return 0
            if i in mem:
                return mem[i]
            skip = dfs(i + 1)
            _, end_i, profit_i = jobs[i]
            next_i = find_next_index(end_i)
            take = profit_i + dfs(next_i)

            mem[i] = max(skip, take)
            return mem[i]

        return dfs(0)
