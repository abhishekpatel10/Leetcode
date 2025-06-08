# Last updated: 6/8/2025, 11:54:56 AM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        r= n -1 
        m = 0
        ans = float('inf')
        while l <= r:
            m = (r+l) //2
            if nums[l] <= nums[r]:
                ans = min(ans,nums[l])
                break
            if nums[l] <= nums[m]:
                ans = min(ans,nums[l])
                l = m +1
            if nums[m] <= nums[r]:
                ans = min(ans,nums[m])
                r = m - 1
        return ans
