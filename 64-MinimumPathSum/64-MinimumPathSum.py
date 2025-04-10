# Last updated: 4/10/2025, 5:00:14 PM
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                else:
                    up = grid[i][j]
                    if i > 0:
                        up += dp[i-1][j]
                    else:
                        up += float('inf')
                    left = grid[i][j]
                    if j >0:
                        left += dp[i][j-1]
                    else:
                        left += float('inf')
                    dp[i][j] = min(left,up)

        return dp[n-1][m-1] 
    
        
