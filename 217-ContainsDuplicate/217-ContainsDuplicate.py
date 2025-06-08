# Last updated: 6/8/2025, 11:54:42 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ss = set()
        n  = len(nums)

        for i in range(n):
            if nums[i] in ss:
                return True
           
            ss.add(nums[i])
        
        return False