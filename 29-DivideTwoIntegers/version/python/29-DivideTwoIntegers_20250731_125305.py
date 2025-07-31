# Last updated: 7/31/2025, 12:53:05 PM
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor:
            return 1
        sign = True
        if dividend < 0 and divisor > 0:
            sign = False
        if dividend >= 0 and divisor < 0:
            sign = False
        ans = 0
        n = abs(dividend)
        m = abs(divisor)
        while n >= m:
            cnt = 0
            while n >= (m <<(cnt+1)):
                cnt+= 1
            ans += 1 << cnt
            n = n - (m * (1<<cnt))
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Correct overflow logic
        result = ans if sign else -ans
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result


    