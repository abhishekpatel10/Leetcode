# Last updated: 7/18/2025, 3:32:41 PM
class Solution:
    def isValid(self, s: str) -> bool:

        stc = []
        for n in s:
            if not stc or n == '(' or n== '[' or n == '{':
                stc.append(n)
            elif stc and stc[-1] == '(' and n == ')':
                stc.pop()
            elif stc and stc[-1] == '[' and n == ']':
                stc.pop()
            elif stc and stc[-1] == '{' and n == '}':
                stc.pop()
            else:
                return False
        if len(stc) > 0:
            return False
        else:
            return True