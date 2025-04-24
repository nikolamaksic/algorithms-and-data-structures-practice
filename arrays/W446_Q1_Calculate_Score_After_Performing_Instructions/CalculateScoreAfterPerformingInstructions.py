class Solution:
    def calculateScore(self, instructions: list[str], values: list[int]) -> int:
        n = len(instructions)
        visited = [0]*n
        res = 0
        i = 0
        while i>=0 and i<n:
            if visited[i]:
                break
            visited[i] = 1
            if instructions[i]=="add":
                res+=values[i]
                i+=1
                continue
            if instructions[i]=="jump":
                i = i + values[i]
        return res