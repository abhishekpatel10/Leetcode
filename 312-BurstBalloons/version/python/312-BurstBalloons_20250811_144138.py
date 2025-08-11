# Last updated: 8/11/2025, 2:41:38 PM
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n+2) for _ in range(n+2)] 
        for i in range(n,0,-1):
            for j in range(1,n+1):
                if i > j :
                    continue
                ans = float('-inf')
                for ind in range(i,j+1):
                    curr = nums[i-1] * nums[ind] * nums[j+1] + dp[i][ind-1] + dp[ind+1][j]
                    ans = max(curr,ans)
                dp[i][j] = ans
        return dp[1][n]
                
        
        

            