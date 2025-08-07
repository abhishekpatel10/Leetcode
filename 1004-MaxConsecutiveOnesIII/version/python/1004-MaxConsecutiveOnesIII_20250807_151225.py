# Last updated: 8/7/2025, 3:12:25 PM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        cnt = 0
        l = 0
        for r in range(n):
            if nums[r] == 0:
                cnt += 1
            while cnt > k:
                if nums[l] == 0:
                    cnt -= 1
                l +=1
            ans = max(ans,r-l + 1)
        return ans
