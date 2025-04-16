# Last updated: 4/16/2025, 7:10:44 PM
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0 for _ in range(amount +1 )] for _ in range(n)]

        for j in range(amount + 1):
            if j % coins[0] == 0:
                dp[0][j] = 1
        for i in range(1,n):
            for j in range(amount +1):
                notpick = dp[i-1][j]
                pick = 0
                if coins[i] <= j:
                    pick = dp[i][j - coins[i]]
                dp[i][j] = pick + notpick
        return dp[n-1][amount]
     
