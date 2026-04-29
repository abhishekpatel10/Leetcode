# Last updated: 4/29/2026, 3:36:46 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        n = len(prices)
4        if n < 2:
5            return 0
6        curr_min = float('inf')
7        max_profit = float('-inf')
8        for i in range(n):
9            curr_min = min(prices[i],curr_min)
10 
11            if prices[i] > curr_min:
12                curr_profit = prices[i] - curr_min
13                max_profit = max(max_profit,curr_profit)
14        if max_profit == float('-inf'):
15            return 0
16        else:
17            return max_profit
18