# Last updated: 6/8/2025, 11:54:01 AM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_avg = 0
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]
        
        max_avg = curr_sum / k

        for i in range( k , n):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]

            curr_avg = curr_sum / k
            max_avg = max(curr_avg , max_avg)
        return max_avg
