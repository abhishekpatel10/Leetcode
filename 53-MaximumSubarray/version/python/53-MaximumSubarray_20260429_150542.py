# Last updated: 4/29/2026, 3:05:42 PM
1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        ansStart = -1
4        ansEnd = -1
5        n = len(nums)
6        maxi = float('-inf')
7        summ = 0
8        for i in range(n):      
9            summ += nums[i]
10            if summ > maxi:
11                maxi = summ
12            if summ < 0:
13                summ = 0
14        return maxi
15        