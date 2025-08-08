# Last updated: 8/8/2025, 4:43:27 PM
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def lower_bound(arr,a):
            r = len(arr) - 1
            l = 0
            while l <=r:
                m = (l+r) // 2
                if arr[m] < a:
                    l = m + 1
                else:
                    r  = m -1
            return l
        n = len(nums)
        if n == 0:
            return 0
        arr = []
        arr.append(nums[0]) 
        for i in range(1,n):
            if arr[-1] < nums[i]:
                arr.append(nums[i])
            else:
                l = lower_bound(arr,nums[i])
                arr[l] = nums[i]
        return len(arr)