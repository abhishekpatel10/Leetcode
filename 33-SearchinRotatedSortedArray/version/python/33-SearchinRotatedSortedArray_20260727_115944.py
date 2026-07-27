# Last updated: 7/27/2026, 11:59:44 AM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        n = len(nums)
4        l = 0
5        r = n - 1
6        m = 0 
7        while l <= r:
8            m = (r+l) // 2
9            if nums[m] == target:
10                return m
11            elif nums[m] >= nums[l]:
12                if nums[l] <= target and target <= nums[m]:
13                    r = m - 1
14                else:
15                    l = m +1
16            else:
17                if nums[r] >= target and target >= nums[m]:
18                    l = m +1
19                else:
20                    r = r -1
21        return -1