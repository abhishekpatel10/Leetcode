# Last updated: 6/8/2025, 11:52:43 AM
class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        openn  =0
        close = 0
        for char in s:
            if char=="(":
                openn += 1
            if char==")":
                close += 1
            curr_ans = openn - close
            ans = max(ans,curr_ans)
        return ans