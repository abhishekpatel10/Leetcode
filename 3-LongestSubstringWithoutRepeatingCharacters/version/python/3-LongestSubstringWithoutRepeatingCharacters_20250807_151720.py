# Last updated: 8/7/2025, 3:17:20 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        ss = set()
        n = len(s)
        l = 0
        for i in range(n):
            while s[i] in ss:
                ss.remove(s[l])
                l += 1
            ss.add(s[i])
            ans = max(ans , i - l + 1)
        return ans