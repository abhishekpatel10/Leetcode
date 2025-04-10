# Last updated: 4/10/2025, 4:51:24 PM
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        return self.solve(n-1,m-1,grid,dp)
    def solve(self,i,j,grid,dp):
        if i == 0 and j == 0:
            return grid[i][j]
        if i < 0 or j < 0 :
            return float('inf')
        if dp[i][j] != -1:
            return dp[i][j]

        
        up = grid[i][j] + self.solve(i-1,j,grid,dp)
        
        left = grid[i][j] + self.solve(i,j-1,grid,dp)
        dp[i][j] = min(up,left)
        
        return dp[i][j]
        
