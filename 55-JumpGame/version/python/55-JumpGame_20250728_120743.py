# Last updated: 7/28/2025, 12:07:43 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        curr_reach = 0
        for i in range(n):
            if curr_reach < i:
                return False
            curr_reach = max(curr_reach,i + nums[i])
        return True

        
        
        