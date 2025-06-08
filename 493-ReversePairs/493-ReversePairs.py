# Last updated: 6/8/2025, 11:54:13 AM
class Solution:
    
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums) - 1
        return self.mergeSort(nums,0,n)
    def mergeSort(self,nums,start,end):
        cnt = 0
        if start >= end:
            return 0
        
        mid = (start + end)//2
        cnt +=self.mergeSort(nums,start,mid)
        cnt +=self.mergeSort(nums,mid+1,end)
        cnt+=self.counts(nums,start,mid,end)
        self.merge(nums,start,mid,end)
        return cnt
    
    def merge(self,nums,start,mid,end):
        left = nums[start:mid+1]
        right = nums[mid+1:end+1]
        i,j= 0,0
        k = start
        while i <len(left) and j <len(right):
            if left[i]<= right[j]:
                nums[k] = left[i]
                i+=1
                k +=1
            else:
                nums[k] = right[j]
                j+=1
                k+=1
        while i <len(left):
            nums[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1
        return nums
    def counts(self,nums,start,mid,end):
        right = mid+1
        cnt = 0
        for i in range(start,mid+1):
            while right <= end and nums[i] > 2 * nums[right]:  
                right +=1
            cnt += right - (mid+1)
        return cnt