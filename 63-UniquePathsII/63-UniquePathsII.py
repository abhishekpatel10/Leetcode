# Last updated: 4/10/2025, 3:44:52 PM
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[-1 for _ in range(m) ] for _ in range(n)]
        if obstacleGrid[0][0] == 1:
            return 0
            
        return self.solve(n-1,m-1,obstacleGrid,dp)
        
    def solve(self,i,j,obstacleGrid,dp):
        if i ==0 and j == 0 :
            return 1
        if i < 0 or j < 0:
            return 0
        if obstacleGrid[i][j] == 1:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        up = 0
        if i > 0:
            up += self.solve(i-1,j,obstacleGrid,dp)
        left = 0
        if j > 0:
            left += self.solve(i,j-1,obstacleGrid,dp)
        dp[i][j] = up + left
        return dp[i][j]