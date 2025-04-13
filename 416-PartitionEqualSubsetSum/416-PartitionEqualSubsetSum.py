# Last updated: 4/13/2025, 2:14:47 PM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        m = sum(nums)
        if m % 2 == 1:
            return False
        target = m //2
        n = len(nums) 
        dp = [[False for _ in range(target +1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True 
        for i in range(1,n):
            for tar in range(1,target+1):
                notpick = dp[i-1][tar]
                pick = False
                if tar >= nums[i]:
                    pick = dp[i-1][tar- nums[i]]
                dp[i][tar] = pick or notpick
        return dp[n-1][target]

        