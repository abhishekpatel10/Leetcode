# Last updated: 9/14/2025, 12:22:50 PM
class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        ans = []
        cnt = 0
        for i in range(len(nums)-1, -1, - 1):
            if cnt == k:
                break
            if nums[i] in ans:
                continue
            ans.append(nums[i])
            cnt += 1
        return ans
