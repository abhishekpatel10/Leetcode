# Last updated: 6/8/2025, 11:53:24 AM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_set = set(jewels)
        ans = 0
        for s in stones:
            if s in hash_set:
                ans +=1
        
        return ans

            
        