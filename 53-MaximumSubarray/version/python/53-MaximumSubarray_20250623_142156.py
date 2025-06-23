# Last updated: 6/23/2025, 2:21:56 PM
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        h = {}
        h[0] = 1
        summ = 0
        maxi = float('-inf')
        n = len(nums)
        for i in range(n):
            summ += nums[i]

            if summ > maxi:
                maxi = summ

        # If sum < 0: discard the sum calculated
            if summ < 0:
                summ = 0
            
        return maxi
