# Last updated: 8/3/2026, 11:20:07 AM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        if not s:
4            return 0
5        ss = set()
6        ans = float('-inf')
7        l =0
8        for r in range(len(s)):
9            while s[r] in ss:
10                ss.remove(s[l])
11                l += 1
12            ans = max(ans,r-l + 1)
13            if not ss or s[r] not in ss:
14                ss.add(s[r])
15            
16                
17        return ans 