# Last updated: 7/30/2025, 7:06:46 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n & n -1 == 0:
            return True
        else:
            return False
        