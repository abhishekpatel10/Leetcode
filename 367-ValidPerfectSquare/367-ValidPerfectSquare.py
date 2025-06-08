# Last updated: 6/8/2025, 11:54:24 AM
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 0
        r = num // 2
        if num == 1:
            return True

        while l <=r:
            m = (r+l) //2
            if m*m == num:
                return True
            elif m*m > num:
                r = m -1
            else:
                l = m + 1
        return False
