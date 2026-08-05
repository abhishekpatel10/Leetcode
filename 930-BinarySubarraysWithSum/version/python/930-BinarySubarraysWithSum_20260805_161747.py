# Last updated: 8/5/2026, 4:17:47 PM
1class Solution:
2    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
3        hm = {0: 1}  # Base case: a prefix sum of 0 has occurred once
4        curr_sum = 0
5        ans = 0
6        
7        for num in nums:
8            curr_sum += num
9            # Check how many times (curr_sum - goal) has appeared
10            ans += hm.get(curr_sum - goal, 0)
11            # Store/update frequency of current prefix sum
12            hm[curr_sum] = hm.get(curr_sum, 0) + 1
13            
14        return ans