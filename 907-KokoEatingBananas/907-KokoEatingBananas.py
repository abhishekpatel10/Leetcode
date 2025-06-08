# Last updated: 6/8/2025, 11:53:16 AM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def func(piles,h):
            ans = 0
            for pile in piles:
                ans += math.ceil(pile/h)
            return ans
        l = 1
        r = max(piles)
        ans = 0
        while l <=r:
            m = (l+r) //2
            min_num = func(piles,m)
            if min_num <= h:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans