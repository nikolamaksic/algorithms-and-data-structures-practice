class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        def dfs(i):
            for j in range(n):
                if isConnected[i][j]==1:
                    isConnected[i][j]=2
                    dfs(j)
        count = 0
        for row in range(n):
            for col in range(n):
                if isConnected[row][col]==1:
                    count+=1
                    dfs(col)
        return count
