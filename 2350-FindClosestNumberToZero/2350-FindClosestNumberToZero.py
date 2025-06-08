# Last updated: 6/8/2025, 11:52:24 AM
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = float('inf')

        for i in nums:
            if abs(i) < abs(max_num):
                max_num = i
        
        if max_num < 0 and abs(max_num) in nums:
            return abs(max_num)
        else:
            return max_num
