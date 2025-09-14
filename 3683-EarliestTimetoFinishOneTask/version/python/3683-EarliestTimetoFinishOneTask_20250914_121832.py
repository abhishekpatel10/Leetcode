# Last updated: 9/14/2025, 12:18:32 PM
class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = float('inf')
        for i in range(len(tasks)):
            summ = tasks[i][0] + tasks[i][1]
            if ans > summ:
                ans = summ
        return ans