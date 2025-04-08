# Last updated: 4/8/2025, 12:16:54 AM
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        prev = nums[0]
        prev2 = 0

        for i in range(1,n):
            pick = nums[i]
            if i > 1:
                pick += prev2
            notpick = prev
            curr = max(pick , notpick)
            prev2 = prev
            prev = curr
        return prev
        
        