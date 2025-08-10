# Last updated: 8/10/2025, 5:33:57 PM
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        c = len(cuts)
        cuts.insert(0,0)
        cuts.append(n)
        cuts.sort()
        dp = [[-1 for _ in range(c+1)] for _ in range(c+1)]
        return self.f(1,len(cuts) - 2,cuts,dp)
    def f(self,i,j,cuts,dp):
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        ans = float('inf')
        for ind in range(i,j+1):
            curr = cuts[j+1] - cuts[i-1] + self.f(i,ind-1,cuts,dp) + self.f(ind+1,j,cuts,dp)
            ans = min(ans,curr)
        dp[i][j] = ans
        return dp[i][j]


        