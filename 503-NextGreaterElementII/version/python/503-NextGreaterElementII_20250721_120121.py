# Last updated: 7/21/2025, 12:01:21 PM
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums) 
        stc = []
        n = len(nums)

        for i in range(2*n-1,-1,-1):
            while stc and nums[i%n] >= stc[-1]:
                stc.pop()
            if i < n and stc:
                ans[i] = stc[-1]
            stc.append(nums[i%n])
        return ans

