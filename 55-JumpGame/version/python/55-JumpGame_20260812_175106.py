# Last updated: 8/12/2026, 5:51:06 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        max_jump = 0
4        for i in range(len(nums)):
5            if i > max_jump:
6                return False
7            max_jump = max(max_jump, i + nums[i])
8            if max_jump >= len(nums) - 1:
9                return True
10
11 
12
13
14
15
16
17        