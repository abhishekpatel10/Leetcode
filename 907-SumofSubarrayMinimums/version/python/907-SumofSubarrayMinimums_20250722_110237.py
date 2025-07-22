# Last updated: 7/22/2025, 11:02:37 AM
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        def psee(arr):
            stc = []
            ans = [-1] * len(arr)
            for i in range(len(arr)):
                while stc and arr[stc[-1]] > arr[i]:
                    stc.pop()
                if stc:
                    ans[i] = stc[-1]
                stc.append(i)
            return ans
        def nsee(arr):
            stc = []
            n = len(arr)
            ans = [n] * len(arr)
            for i in range(n-1, -1 ,-1):
                while stc and arr[stc[-1]]  >= arr[i]:
                    stc.pop()
                if stc:
                    ans[i] = stc[-1]
                stc.append(i)
            return ans
        total = 0
        pse = psee(arr)
        nse = nsee(arr)
        mod = 10**9 + 7
        for i in range(len(arr)):
            left = i - pse[i]
            right = nse[i] - i
            total = (total + arr[i] * left * right) % mod
        return total