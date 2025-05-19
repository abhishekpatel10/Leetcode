# Last updated: 5/19/2025, 5:34:22 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        m = 0 
        while l <= r:
            m = (r+l) // 2
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]:
                if nums[l] <= target and target <= nums[m]:
                    r = m - 1
                else:
                    l = m +1
            else:
                if nums[r] >= target and target >= nums[m]:
                    l = m +1
                else:
                    r = r -1
        return -1