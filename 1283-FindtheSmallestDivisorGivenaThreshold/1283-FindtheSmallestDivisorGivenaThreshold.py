# Last updated: 5/21/2025, 5:00:29 PM
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def func(nums,m):
            ans = 0 
            for n in nums:
                ans += ceil(n/m)
            return ans
        l = 1
        r = max(nums)
        ans = 0
        while l <=r:
            m = (r+l)//2
            total_min = func(nums,m)
            if total_min <= threshold:
                ans = m
                r = m - 1 
            else:
                l = m + 1
        return ans
        