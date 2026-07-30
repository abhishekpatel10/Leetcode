# Last updated: 7/30/2026, 12:11:08 PM
1class Solution:
2    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
3        l = min(bloomDay)
4        r = max(bloomDay)
5        ans = float('inf')
6        def func(mid,m,k):
7            count = 0  # count of consecutive bloomed flowers
8            bouquets = 0  # number of bouquets formed
9
10            for bloom in bloomDay:
11                if bloom <= mid:
12                    count += 1
13                    if count == k:
14                        bouquets += 1  # one bouquet formed
15                        count = 0
16                else:
17                    count = 0  # reset if a flower is not ready
18
19            return bouquets >= m
20                
21        if (m*k) > len(bloomDay):
22            return -1
23        while l <=r:
24            mid = (r+l)//2
25            curr = func(mid,m,k)
26            if curr:
27                ans = mid
28                r = mid - 1
29            else:
30                l = mid + 1
31        return ans