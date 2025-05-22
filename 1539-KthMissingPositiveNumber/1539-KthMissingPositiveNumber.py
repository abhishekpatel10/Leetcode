# Last updated: 5/22/2025, 1:14:01 AM
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        n = len(arr)
        r = n - 1
        ans = 0
        for i in range(n):
            if arr[i] <= k:
                k += 1
            else:
                break
        return k