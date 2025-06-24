# Last updated: 6/23/2025, 7:33:30 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = {0:1}
        pre_sum = 0
        ans = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            rem = pre_sum - k
            if rem in h:
                ans += h[rem]
            if pre_sum not in h:
                h[pre_sum] = 1
            else:
                h[pre_sum] += 1
        return ans
