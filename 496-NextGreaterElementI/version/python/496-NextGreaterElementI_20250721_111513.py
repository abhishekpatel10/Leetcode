# Last updated: 7/21/2025, 11:15:13 AM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums2)
        stc = []
        n = len(nums2)
        for i in range(n-1,-1,-1):
            while stc and stc[-1] <= nums2[i]:
                stc.pop()
            if stc:
                ans[i] = stc[-1]
            stc.append(nums2[i])
        res = []
        for num in nums1:
            index = nums2.index(num) 
            res.append(ans[index])
        return res
        