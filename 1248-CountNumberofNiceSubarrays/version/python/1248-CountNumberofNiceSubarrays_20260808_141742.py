# Last updated: 8/8/2026, 2:17:42 PM
1class Solution:
2    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
3        return self.sol(nums,k) - self.sol(nums,k-1)
4        
5    def sol(self,nums,k):
6        cnt = 0 
7        n = len(nums)
8        l = 0
9        ans = 0
10        for r in range(n):
11            if nums[r] %2 == 1:
12                cnt += 1
13            while cnt > k:
14                if nums[l] % 2 == 1:
15                    cnt -= 1
16                l += 1
17            ans += (r - l) + 1
18        return ans