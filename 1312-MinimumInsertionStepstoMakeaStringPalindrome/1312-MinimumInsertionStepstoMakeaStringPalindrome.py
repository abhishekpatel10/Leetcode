# Last updated: 4/16/2025, 8:04:05 PM
class Solution:
    def minInsertions(self, s: str) -> int:
        s1 = s[::-1]
        m = len(s)
        n = len(s1)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[j-1] == s1[i-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        
        final_ans = m - dp[n][m]
        return final_ans
    