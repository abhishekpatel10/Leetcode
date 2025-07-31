# Last updated: 7/31/2025, 2:11:30 PM
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for prev in range(i - 1, -2 , -1):
                notpick = 0 + dp[i+1][prev+1]
                if prev == -1 or nums[i] > nums[prev]:
                    notpick = max(notpick,1+dp[i+1][i+1])
                dp[i][prev+1] = notpick
        return dp[0][0]
        