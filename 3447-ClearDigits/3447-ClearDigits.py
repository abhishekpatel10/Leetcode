# Last updated: 6/8/2025, 11:52:13 AM
class Solution:
    def clearDigits(self, s: str) -> str:
        stc = []
        for n in s:
            if n.isdigit():
                if stc:
                    stc.pop()
            else:
                stc.append(n)

        return ''.join(stc)