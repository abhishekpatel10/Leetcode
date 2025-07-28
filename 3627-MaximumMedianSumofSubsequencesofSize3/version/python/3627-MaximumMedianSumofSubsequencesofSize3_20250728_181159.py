# Last updated: 7/28/2025, 6:11:59 PM
class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 2
        ans = 0
        while l < r:
            ans += nums[r]
            r -= 2
            l += 1
        return ans