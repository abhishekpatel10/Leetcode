# Last updated: 8/3/2026, 11:35:33 AM
1class Solution:
2    def longestOnes(self, nums: List[int], k: int) -> int:
3        ans = 0
4        n = len(nums)
5        l = 0
6        cnt = 0
7        for r in range(n):
8            if nums[r] == 1:
9                ans = max(ans,r - l + 1)
10            else:
11                cnt += 1
12
13                if cnt <= k:
14                    ans = max(ans,r - l + 1)
15                    continue
16                else:
17                    while cnt != k:
18                        if nums[l] ==0:
19                            cnt -=1
20                        l += 1
21        return ans