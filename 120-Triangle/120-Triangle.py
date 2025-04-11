# Last updated: 4/11/2025, 12:17:55 AM
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        m = len(triangle[n - 1])
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        

        return self.solve(triangle,0,0,n,dp)
    
    def solve(self,triangle,i,j,n,dp):
        if i == n-1:
            return triangle[i][j]
        if dp[i][j] != -1:
            return dp[i][j]
        down = triangle[i][j] + self.solve(triangle,i+1,j,n,dp)
        diag = triangle[i][j] + self.solve(triangle,i+1,j+1,n,dp)
        dp[i][j] = min(down,diag)
        return dp[i][j]
    
        