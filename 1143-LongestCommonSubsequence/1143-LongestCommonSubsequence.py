# Last updated: 4/15/2025, 2:39:37 AM
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        return self.solve(m-1,n-1,text1,text2,dp)
    def solve(self,m,n,text1,text2,dp):
        if m < 0 or n < 0:
            return 0
        if dp[m][n] != -1:
            return dp[m][n]
        if text1[m] == text2[n]:
            return 1 + self.solve(m-1,n-1,text1,text2,dp)
        dp[m][n] = max(self.solve(m-1,n,text1,text2,dp),self.solve(m,n-1,text1,text2,dp))
        return dp[m][n]