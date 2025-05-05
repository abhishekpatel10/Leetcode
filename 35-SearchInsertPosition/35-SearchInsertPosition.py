# Last updated: 5/4/2025, 8:52:43 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = 0
        ans = target
        while l <=r:
            m = (r+l) // 2
            if nums[m] >= target:
                ans = m
                r = m -1
            else:
                l = m + 1
        return l
                
        
        
            