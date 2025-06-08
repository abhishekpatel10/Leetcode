# Last updated: 6/8/2025, 11:55:04 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for n in nums:
            xor = xor ^ n
        return xor
