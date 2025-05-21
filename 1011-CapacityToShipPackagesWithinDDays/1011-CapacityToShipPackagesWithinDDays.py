# Last updated: 5/21/2025, 5:13:49 PM
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def func(weights,m):
            ans = 1
            cnt = 0
            for w in weights:
                if cnt + w<= m:
                    cnt += w
                else:
                    ans += 1
                    cnt = w

            return ans
        l = max(weights)
        ans = 0
        r = sum(weights)

        while l <= r:
            m = (r+l) // 2
            total_min = func(weights,m)
            if total_min <= days:
                ans = m
                r = m -1
            else:
                l = m + 1
        return ans