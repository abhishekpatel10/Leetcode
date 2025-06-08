# Last updated: 6/8/2025, 11:52:47 AM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        mid = n
        ans =[]
        j = 1
        while i < mid and mid < len(nums):
            ans.append(nums[i])
            i += 1
            ans.append(nums[mid])
            mid += 1
        return ans


