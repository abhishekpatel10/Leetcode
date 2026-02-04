# Last updated: 2/4/2026, 12:00:44 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        ans = ""
4        n = len(s)
5        maxlen = 0
6        for i in range(n):
7            l = i
8            r = i
9            while l >= 0 and r < len(s) and s[l] == s[r]:
10                if (r - l )+ 1 > maxlen:
11                    maxlen = r - l + 1
12                    ans = s[l:r+1]
13                l -= 1
14                r += 1
15            l = i
16            r = i + 1
17            while l >= 0 and r < len(s) and s[l] == s[r]:
18                if (r - l )+ 1 > maxlen:
19                    maxlen = r - l + 1
20                    ans = s[l:r+1]
21                l -= 1
22                r += 1
23        return ans