# Last updated: 6/8/2025, 11:52:16 AM
class Solution:
    def minimumSteps(self, s: str) -> int:
        swap,black = 0 , 0

        for ball in s:
            if ball == "0":
                swap += black
            else:
                black += 1
        return swap
