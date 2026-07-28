# Last updated: 7/28/2026, 4:37:15 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l = 0
4        r = len(nums) - 1
5        ans = float('inf')
6        while l <= r:
7            mid = (r+l) // 2
8            if nums[mid] < ans:
9                ans = nums[mid]
10            if nums[l] <= nums[mid]:
11                ans = min(ans,nums[l])
12                l = mid + 1
13            if nums[mid] <= nums[r]:
14                ans = min(ans,nums[mid])
15                r = mid - 1
16        return ans