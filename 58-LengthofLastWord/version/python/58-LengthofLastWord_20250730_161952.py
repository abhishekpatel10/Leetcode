# Last updated: 7/30/2025, 4:19:52 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str(s.rstrip())
        print(s)
        n = len(s)
        i = n - 1
        while s[i] == " ":
            i -= 1
            continue
        ans = 0
        while s[i] != " ":
            ans += 1
            if ans == len(s):
                break
            i -=1
        return ans
        

        