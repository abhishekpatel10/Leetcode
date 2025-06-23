# Last updated: 6/23/2025, 2:16:39 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        h = {}
        h[0] = 1
        presum = 0
        ans = float('-inf')
        
        for i in range(len(nums)):
            presum += nums[i]
            ans = max(presum , ans)
            if presum < 0:
                presum = 0
            
        return ans
