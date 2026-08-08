# Last updated: 8/8/2026, 5:46:20 PM
1class Solution:
2    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
3        return self.solve(nums,k) - self.solve(nums,k-1)
4    def solve(self,nums,k):
5        ans = 0
6        if k <0:
7            return 0
8        l = 0
9        n = len(nums)
10        hash_map = {}
11        for r in range(n):
12            hash_map[nums[r]] = hash_map.get(nums[r], 0) + 1
13            while len(hash_map) > k:
14                hash_map[nums[l]] -= 1
15                if hash_map[nums[l]] == 0:
16                    del hash_map[nums[l]]
17                l += 1
18            ans += (r - l + 1)
19        return ans
20            