# Last updated: 6/8/2025, 11:54:29 AM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                j = i
                break
        if j == -1:
            return 
        for i in range(j+1,n):
            if nums[i] != 0 :
                nums[j] ,nums[i] = nums[i] , nums[j]
                j +=1

        