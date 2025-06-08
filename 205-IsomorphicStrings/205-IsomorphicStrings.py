# Last updated: 6/8/2025, 11:54:50 AM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h1 = {}
        h2 = {}
        for i in range(len(s)):
            c1 ,c2= s[i], t[i]
            if (c1 in h1 and h1[c1] != c2 )or (c2 in h2 and h2[c2] != c1):
                return False
            h1[c1] = c2
            h2[c2] = c1
        return True