# Last updated: 8/21/2025, 12:29:21 PM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        stc = []
        ans = [-1] * n
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
        

        