# Last updated: 4/7/2025, 10:27:13 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = [-1] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            left = dp[i-1]
            right = nums[i] + dp[i-2]
            dp[i] = max(left,right)
        return dp[n- 1]
        
        