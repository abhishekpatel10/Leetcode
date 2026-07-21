# Last updated: 7/21/2026, 12:23:15 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums) 
4        dp = [-1] * (n+1)
5        dp[0] = nums[0]
6        for i in range(1,n):
7            pick = nums[i]
8            if i - 2 > -1: 
9                pick = nums[i] + dp[i-2]
10            notpick = dp[i-1]
11            dp[i] = max(pick,notpick)
12
13        return dp[n - 1]
14
15    
16    