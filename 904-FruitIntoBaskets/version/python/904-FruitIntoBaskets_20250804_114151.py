# Last updated: 8/4/2025, 11:41:51 AM
from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        ans = float('-inf')
        n = len(fruits)
        hashMap = defaultdict(int)
        for r in range(n):
            hashMap[fruits[r]] += 1
            while len(hashMap) > 2:
                hashMap[fruits[l]] -= 1
                if hashMap[fruits[l]] == 0:
                    del hashMap[fruits[l]]
                l +=1
            ans = max(ans,r-l+1)
        return ans
