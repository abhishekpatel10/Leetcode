# Last updated: 8/19/2025, 12:29:41 PM
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n-1,-1,-1):
            length = 0
            maxi = float('-inf')
            ans = float('-inf')
            for j in range(i,min(i+k,n)):
                length += 1
                maxi = max(maxi,arr[j])
                summ = (length * maxi) + dp[j+1]
                ans = max(summ,ans)
                dp[i] = ans
        return dp[0]

    
