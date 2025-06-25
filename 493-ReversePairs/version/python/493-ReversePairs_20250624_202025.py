# Last updated: 6/24/2025, 8:20:25 PM
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        n = len(nums)
        j = 0
        for i ,x in enumerate(nums):
            if x == key:
                up = min(n-1,i+k)
                j = max(j,i-k)
                while j <=up:
                    ans.append(j)
                    j+=1
        return ans
        
            
