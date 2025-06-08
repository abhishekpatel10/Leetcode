# Last updated: 6/8/2025, 11:52:53 AM
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        ans = 0
        curr_sum = 0

        for i in range(k):
            curr_sum += arr[i]
        if curr_sum/k >= threshold :
            ans += 1
        
        for i in range(k , n):
            curr_sum -= arr[i - k]
            curr_sum += arr[i]

            if curr_sum /k>= threshold :
                ans += 1
        return ans
