# Last updated: 6/8/2025, 11:54:14 AM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxCount = 0
        for n in nums:
            if n == 1:
                count += 1

            else:
                count = 0
            if maxCount < count:
                maxCount = count
        return maxCount 