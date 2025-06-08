# Last updated: 6/8/2025, 11:54:14 AM
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()

        count = 0
        j = 0
        i = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i+= 1
            j += 1
        
        return count