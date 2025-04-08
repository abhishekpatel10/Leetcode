# Last updated: 4/8/2025, 12:42:01 AM
class Solution:
    def rob(self, nums: List[int]) -> int:
        arr1 = []
        arr2 = []
        n = len(nums)
        
        if n == 1:
            return nums[0]
        for i in range(len(nums)):
            if i != 0:
                arr1.append(nums[i])
            if i != n -1:
                arr2.append(nums[i])
        firsthalf = self.solve(arr1)
        secondhalf = self.solve(arr2)

        return max(firsthalf,secondhalf)
    def solve(self,arr):
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
        dp = [0] * n
        dp[0] = arr[0]
        for i in range(1,n):
            pick = arr[i]
            if i > 1:
                pick += dp[i-2]
            notpick = dp[i-1]
            dp[i] = max(pick,notpick)
        return dp[-1]
