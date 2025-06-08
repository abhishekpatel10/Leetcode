# Last updated: 6/8/2025, 11:54:28 AM
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = {}

        for num in nums:
            if num in h :
                return num
            else:
                h[num] = 1
        