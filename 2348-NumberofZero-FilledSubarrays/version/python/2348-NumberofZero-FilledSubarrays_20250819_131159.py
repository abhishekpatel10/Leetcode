# Last updated: 8/19/2025, 1:11:59 PM
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        cnt = 0
        for n in nums:
            if n == 0:
                cnt += 1
            else:
                total += cnt * (cnt+1) //2
                cnt = 0
        total += cnt * (cnt+1) // 2
        return total


