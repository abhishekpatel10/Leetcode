# Last updated: 9/13/2025, 12:48:39 PM
class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        avg = total / n
        x = floor(avg) + 1
        if x <= 0:
            x = 1
        for num in nums:
            if x not in nums:
                return x

            else:
                x += 1