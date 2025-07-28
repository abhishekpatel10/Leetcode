# Last updated: 7/28/2025, 2:04:49 PM
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda interval:interval[1])
        ans = 0
        end = float('-inf')
        n = len(intervals)
        for interval in intervals:
            if interval[0] >= end:
                end = interval[1]
            else:
                ans += 1


        return ans
