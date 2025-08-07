# Last updated: 8/7/2025, 3:33:38 PM
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        n = len(nums)
        l = 0
        summ = 0
        mpp = defaultdict(int)
        mpp[0] = 1
        for r in range(n):
            summ += nums[r]
            remove = summ - goal

            ans += mpp[remove]
            mpp[summ] += 1
        return ans
            
        return ans