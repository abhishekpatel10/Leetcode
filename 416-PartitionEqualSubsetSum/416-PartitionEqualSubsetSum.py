# Last updated: 4/12/2025, 7:42:21 PM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        m = sum(nums)
        if m % 2 == 1:
            return False
        target = m //2
        n = len(nums) 
        dp = [[-1 for _ in range(target +1)] for _ in range(n)]

        return self.solve(n-1,target,nums,dp)
    def solve(self,n,target,nums,dp):
        if n == 0 and target == 0 :
            return True
        if n == 0 and target > 0:
            return nums[0] == target
        if dp[n][target] != -1:
            return dp[n][target]
        notpick = self.solve(n-1,target,nums,dp)
        pick = False
        if target >= nums[n]:
            pick = self.solve(n-1,target- nums[n],nums,dp)
        dp[n][target] = pick or notpick
        return dp[n][target]