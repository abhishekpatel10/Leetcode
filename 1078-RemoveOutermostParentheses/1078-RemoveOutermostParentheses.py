# Last updated: 6/8/2025, 11:53:06 AM
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res , opened = [] , 0
        for c in s:
            if c == '(' and opened > 0 :
                res.append(c)
            if c == ')' and opened > 1:
                res.append(c)
            if c == '(':
                opened += 1
            else:
                opened -= 1
        return "".join(res)