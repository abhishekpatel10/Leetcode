# Last updated: 6/8/2025, 11:54:36 AM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        left = 1
        
        for l in range(n):
            ans[l]*= left
            left *=nums[l]
        right = 1
        for l in range(n-1, -1,-1):
            ans[l]*= right
            right *=nums[l]

        return ans
