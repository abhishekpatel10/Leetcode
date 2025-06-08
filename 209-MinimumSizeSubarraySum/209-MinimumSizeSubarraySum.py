# Last updated: 6/8/2025, 11:54:47 AM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        summ = 0
        min_len = float('inf')
        

        for r in range(n):
            summ += nums[r]
            while summ >= target:
                min_len = min(min_len, r -l +1)
                summ -= nums[l]
                l += 1
        return min_len if min_len < float('inf') else 0
            
            
            
            
        return max_len