# Last updated: 6/8/2025, 11:52:44 AM
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        h = len(arr) - 1
        while l <= h :
            m = (l+h) // 2
            missing = arr[m] - m
            if missing <= k:
                l = m + 1
            else:
                h = m - 1
        return l + k