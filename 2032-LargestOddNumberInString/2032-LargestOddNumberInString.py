# Last updated: 6/8/2025, 11:52:32 AM
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) %2 == 1:
                return num[:i+1]
        return ""