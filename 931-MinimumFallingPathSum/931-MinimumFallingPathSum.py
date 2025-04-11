# Last updated: 4/11/2025, 1:20:04 AM
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        curr_min = float('inf')
        dp = [[0 for _ in range(n)]for _ in range(n)]
        for i in range(n):
            dp[0][i] = matrix[0][i]
        for i in range(1,n):
            for j in range(n):
                up = matrix[i][j] + dp[i-1][j]
                
                downleft = matrix[i][j]
                if j - 1 >= 0:
                    downleft += dp[i-1][j-1]
                else:
                    downleft += float('inf') 
                downright = matrix[i][j]
                if j+1 <n:
                    
                    downright += dp[i-1][j+1]
                else:
                    downright += float('inf')
                dp[i][j] = min(up,downleft,downright)
                

        return min(dp[n-1])
