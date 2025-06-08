# Last updated: 6/8/2025, 11:54:16 AM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        counts = [0] * 26
        l = 0

        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1
            while ( (r- l )+1 - max(counts) > k):
                counts[ord(s[l]) - 65] -=1
                l +=1
            
            w = (r - l ) +1
            max_len = max(max_len , w)
        
        return max_len