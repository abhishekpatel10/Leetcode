# Last updated: 6/23/2025, 2:32:55 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = float('inf')
        ans = 0
        for i in range(n):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] > buy:
                curr_profit = prices[i] - buy
                ans = max(ans,curr_profit)
        return ans