# Last updated: 6/8/2025, 11:55:12 AM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        a = prices[0]
        n = len(prices)
        min_prices = float('inf')

        for price in prices:
            if price < min_prices:
                min_prices = price
            profit = price - min_prices

            if profit > max_profit:
                max_profit = profit
        return max_profit 

        
    
        

        

    

        