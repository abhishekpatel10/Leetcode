# Last updated: 8/19/2025, 12:26:26 PM
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        def func(i,dp):
            if i == n:
                return 0 
            if dp[i] != -1:
                return dp[i]
            length = 0
            maxi = float('-inf')
            ans = float('-inf')
            for j in range(i,min(i+k,n)):
                length += 1
                maxi = max(maxi,arr[j])
                summ = (length * maxi) + func(j+1,dp)
                ans = max(summ,ans)
                dp[i] = ans
            return dp[i]
        dp = [-1] * n
        return func(0,dp)
