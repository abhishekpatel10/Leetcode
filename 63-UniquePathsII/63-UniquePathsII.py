# Last updated: 4/10/2025, 4:08:18 PM
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0 for _ in range(m) ] for _ in range(n)]
        if obstacleGrid[0][0] == 1:
            return 0
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    up = 0
                    if i > 0:
                        up += dp[i-1][j]
                    left = 0
                    if j > 0:
                        left += dp[i][j-1]
                    dp[i][j] = up + left
        return dp[n-1][m-1]

            
        