# Last updated: 7/31/2025, 2:16:56 PM
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        next_dp = [0] * (n + 1)
        for i in range(n-1,-1,-1):
            curr = [0] * (n + 1)
            for prev in range(i - 1, -2 , -1):
                notpick = 0 + next_dp[prev+1]
                if prev == -1 or nums[i] > nums[prev]:
                    notpick = max(notpick,1+next_dp[i+1])
                curr[prev+1] = notpick
            next_dp = curr
        return next_dp[0]
        