# Last updated: 6/8/2025, 11:52:21 AM
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] != nums[i+1]:
                continue
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        print(nums)

        j = -1
        for i in range(n):
            if nums[i] == 0:
                j = i
                break
        if j == -1:
            return nums
        for i in range(j+1,n):
            if nums[i] != 0:
                nums[j],nums[i] = nums[i],nums[j]
                j+=1
        return nums