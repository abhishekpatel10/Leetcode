# Last updated: 8/8/2025, 2:25:40 PM
class Solution:
    def soupServings(self, n: int) -> float:
        units = math.ceil(n / 25)
        if units >= 200:
            return 1.0

        dp = [[-1.0] * (units + 1) for _ in range(units + 1)]
        ops = [(4, 0), (3, 1), (2, 2), (1, 3)]

        def prob(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            if dp[a][b] != -1.0:   
                return dp[a][b]

            res = 0.0
            for da, db in ops:
                res += 0.25 * prob(max(0, a - da), max(0, b - db))

            dp[a][b] = res
            return res

        return prob(units, units)
        
        