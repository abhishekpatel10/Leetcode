# Last updated: 5/19/2025, 5:55:42 PM
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l = 0
        r = n - 1
        m = 0
        while l <= r:
            m = (r+l)//2
            
            if nums[m] == target:
                return True
            if nums[l] == nums[m] and nums[m] == nums[r]:
                l = l+1
                r = r-1
                continue
            if nums[l] <= nums[m]:
                if nums[l] <= target and target <= nums[m]:
                    r = m - 1
                else:
                    l = m +1
            else:
                if nums[m] <= target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m -1
        return False