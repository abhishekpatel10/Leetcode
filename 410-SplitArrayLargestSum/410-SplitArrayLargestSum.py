# Last updated: 6/8/2025, 11:54:19 AM
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def func(nums,m):
            curr = 1
            curr_sum = 0
            for i in range(len(nums)):
                if nums[i] + curr_sum <= m:
                    curr_sum += nums[i]
                else:
                    curr +=1
                    curr_sum = nums[i]
            return curr

        l = max(nums)
        r = sum(nums)
        while l <= r:
            m = (r+l) // 2
            tp = func(nums,m)
            if tp <=k:
                r = m  - 1
            else:
                l = m + 1
        return l