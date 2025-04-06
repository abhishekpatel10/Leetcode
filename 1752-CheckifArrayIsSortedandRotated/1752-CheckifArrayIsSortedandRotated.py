# Last updated: 4/6/2025, 1:23:00 AM
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                count += 1
            if count > 1:
                return False
        return True