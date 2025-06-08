# Last updated: 6/8/2025, 11:52:29 AM
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        left = []
        right =[] 
        mid=[]

        for i in range(n):
            if nums[i] > pivot:
                right.append(nums[i])
            elif nums[i] == pivot:
                mid.append(nums[i])
            else:
                left.append(nums[i])
        return left + mid + right
        
