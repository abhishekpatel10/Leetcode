# Last updated: 5/21/2025, 4:45:11 PM
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def func(bloomDay,mid,m,k):
            cnt = 0
            ans = 0
            for b in bloomDay:
                if b <= mid :
                    cnt += 1
                else:
                    ans += floor(cnt/k)
                    cnt = 0
            ans += floor(cnt/k)
            if ans >= m:
                return True
            else:
                return False
        n = len(bloomDay)
        totalflowers = m * k
        if n < m * k:
            return -1
        
        l = min(bloomDay)
        r = max(bloomDay)
        ans = 0
        while l <= r:
            mid = (r+l) // 2
            total_min = func(bloomDay,mid,m,k)
            if total_min:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        if ans > 0:
            return ans
        else:
            return -1

