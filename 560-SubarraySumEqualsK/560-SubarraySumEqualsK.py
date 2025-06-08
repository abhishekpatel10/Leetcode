# Last updated: 6/8/2025, 11:54:06 AM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = {0:1}
        preSum = 0
        counts = 0
        for i in range(len(nums)):
            preSum += nums[i]

        # Calculate x-k:
            remove = preSum - k

        
            counts += h.get(remove,0)

            # Update the count of prefix sum
            # in the map.
            h[preSum] = h.get(preSum,0) + 1
            
        return counts

            