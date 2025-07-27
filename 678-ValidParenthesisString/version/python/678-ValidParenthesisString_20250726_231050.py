# Last updated: 7/26/2025, 11:10:50 PM
class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        for ss in s:
            if ss == '(':
                low += 1
                high +=1
            elif ss == ')':
                low -=1
                high -=1
            else:
                low -= 1
                high += 1
            if low < 0:
                low = 0
            if high < 0 :
                return False
        return low == 0