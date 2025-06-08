# Last updated: 6/8/2025, 11:53:19 AM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
            
        return goal in s+s