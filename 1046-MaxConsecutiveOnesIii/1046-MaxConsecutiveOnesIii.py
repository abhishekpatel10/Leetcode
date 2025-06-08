# Last updated: 6/8/2025, 11:53:09 AM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        n = len(nums)
        l = 0
        max_zeros = 0

        for r in range(n):
            if nums[r] == 0:
                max_zeros += 1

            while max_zeros > k:
                if nums[l] == 0:
                    max_zeros -= 1
                l +=1
            
            w = r - l +1 
            max_len = max(w , max_len)
        return max_len