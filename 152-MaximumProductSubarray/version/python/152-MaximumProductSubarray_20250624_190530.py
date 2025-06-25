# Last updated: 6/24/2025, 7:05:30 PM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        suff = 1
        pre = 1
        n = len(nums)
        ans = float('-inf')
        for i in range(n):
            if suff == 0:
                suff = 1
            if pre == 0:
                pre = 1
            pre *= nums[i]
            suff *= nums[n-i-1]
            ans = max(ans,max(pre,suff))
        return ans