# Last updated: 8/1/2025, 11:07:22 AM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        m = total % 2 
        n = total // 2
        if m == 1:
            return False
        dp = [False] * (n+1)
        
        dp[0] = True
        if nums[0] <= n:
            dp[nums[0]] = True
        for i in range(1,len(nums)):
            temp = [False] * (n+1)
            temp[0] = True
            for target in range(1,n+1):
                notpick = dp[target]
                pick = False
                if nums[i] <= target:
                    pick = dp[target - nums[i]] 
                temp[target] = pick or notpick
            dp = temp
        return dp[n]

        