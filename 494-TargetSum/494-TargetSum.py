# Last updated: 4/16/2025, 6:53:38 PM
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        totalsum = sum(nums)
        if totalsum - target < 0:
            return 0
        if (totalsum - target) % 2 == 1:
            return 0
        s2 = (totalsum - target) // 2
        dp = [[0 for _ in range(s2+1)]for _ in range(n)]
        if nums[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
        if nums[0] != 0 and nums[0] <= s2:
            dp[0][nums[0]] = 1
        for i in range(1,n):
            for j in range(s2+1):
                notpick = dp[i-1][j]
                pick = 0
                if nums[i] <= j:
                    pick = dp[i-1][j - nums[i]]
                dp[i][j] = pick + notpick
        return dp[n-1][s2]
    
    
        