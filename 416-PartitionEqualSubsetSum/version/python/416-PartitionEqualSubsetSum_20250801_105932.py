# Last updated: 8/1/2025, 10:59:32 AM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        m = total % 2 
        n = total // 2
        if m == 1:
            return False
        dp = [[False for _ in range(n+1)] for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0] = True
        if nums[0] <= n:
            dp[0][nums[0]] = True
        for i in range(len(nums)):
            for target in range(n+1):
                notpick = dp[i-1][target]
                pick = False
                if nums[i] <= target:
                    pick = dp[i-1][target - nums[i]] 
                dp[i][target] = pick or notpick
        return dp[len(nums)-1][n]

        