# Last updated: 6/8/2025, 11:52:20 AM
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = set()
        max_sum = 0
        curr_sum = 0
        l = 0
        for r in range(n):
            while nums[r] in s or r - l + 1 > k:
                s.remove(nums[l])
                curr_sum -= nums[l]
                l+= 1
            s.add(nums[r])
            curr_sum += nums[r]

            if r - l + 1 == k:
                max_sum = max(curr_sum , max_sum)
        return max_sum

            
        
        


        