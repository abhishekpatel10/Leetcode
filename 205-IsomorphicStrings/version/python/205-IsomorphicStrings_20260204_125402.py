# Last updated: 2/4/2026, 12:54:02 PM
1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        h1 = {}
4        h2 = {}
5        for i in range(len(s)):
6            c1,c2 = s[i],t[i]
7            if (c1 in h1 and h1[c1] != c2) or (c2 in h2 and h2[c2] != c1):
8                return False
9            h1[c1] = c2
10            h2[c2] =c1
11        return True