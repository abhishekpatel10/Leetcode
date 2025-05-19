# Last updated: 5/19/2025, 5:18:49 PM
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0 
        n = len(nums)
        r = len(nums) -1
        first = n
        m = 0
        while l <=r:
            m = (r+l) // 2
            if nums[m] >= target:
                first = m
                r = m - 1                
            else:
                l = m +1
        if first == n or nums[first] != target:
            return [-1, -1]
        l = 0 
        second = len(nums)
        r = len(nums) - 1
        mid  = 0
        while l <= r:
            mid = (r+l) // 2
            if nums[mid] > target:
                second = mid
                r = mid - 1
            else:
                l = mid +  1
        return [first, second - 1]
