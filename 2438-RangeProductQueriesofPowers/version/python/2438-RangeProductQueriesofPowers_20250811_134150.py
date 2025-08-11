# Last updated: 8/11/2025, 1:41:50 PM
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        MOD = 10**9 + 7
        bit = 0
        while n > 0:
            if n & 1:
                powers.append(1 << bit)  
            n >>= 1
            bit += 1
        powers.sort()
        prefix = [1]
        for p in powers:
            prefix.append((prefix[-1] * p) % MOD)
        def modinv(x):
            return pow(x, MOD - 2, MOD)
        
        ans = []
        for l, r in queries:
            prod = (prefix[r + 1] * modinv(prefix[l])) % MOD
            ans.append(prod)

        return ans