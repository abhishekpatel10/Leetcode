# Last updated: 6/8/2025, 11:54:33 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = Counter(s)
        t1 = Counter(t)

        return s1 == t1
        
        