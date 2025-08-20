# Last updated: 8/20/2025, 12:44:39 PM
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def dfs(i,j,dp):
            if i < 0 or j < 0 or matrix[i][j] == 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] =  1 + min(dfs(i-1,j,dp),dfs(i,j-1,dp) ,dfs(i-1,j-1,dp))
            return dp[i][j]
        total = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                total += dfs(i,j,dp)
        return total