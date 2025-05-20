# Last updated: 5/20/2025, 5:59:00 PM
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[1] != nums[0]:
            return nums[0]
        if nums[n - 2] != nums[n - 1]:
            return nums[n-1]
        l = 1
        r = n- 2
        m = 0
        while l <= r:
            m = (r+l) // 2
            if nums[m] != nums[m - 1] and nums[m] != nums[m+1]:
                return nums[m]
            elif m % 2 == 1 and nums[m-1] == nums[m] or m%2 == 0 and nums[m] == nums[m+1]:
                l = m+1
            else:
                r = m -1 
                