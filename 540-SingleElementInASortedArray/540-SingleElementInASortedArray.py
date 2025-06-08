# Last updated: 6/8/2025, 11:54:10 AM
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        if r == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[r-2] != nums[r-1]:
            return nums[r-1]
        while l <= r:
            m = (r+l) // 2
            if nums[m] != nums[m-1] and nums[m] != nums[m+1]:
                return nums[m]
            if m %2 == 1 and nums[m] == nums[m-1]or m % 2 == 0 and nums[m] == nums[m+1]:
                l = m +1
            else:
                r = m - 1
        