# Last updated: 7/21/2026, 3:00:49 PM
1class Solution:
2    def findContentChildren(self, g: List[int], s: List[int]) -> int:
3        
4        g.sort()
5        s.sort()
6
7        count = 0
8        j = 0
9        i = 0
10        while i < len(g) and j < len(s):
11            if g[i] <= s[j]:
12                count += 1
13                i+= 1
14            j += 1
15        
16        return count