# Last updated: 6/8/2025, 11:55:10 AM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        R = len(s) - 1
        L = 0

        while L < R:
            if not s[L].isalnum():
                L += 1
                continue
            if not s[R].isalnum():
                R -= 1
                continue
            if s[L].lower() != s[R].lower():
                return False
        
            L+=1
            R-=1
        return True

