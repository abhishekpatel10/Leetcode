# Last updated: 8/7/2025, 2:52:04 PM
class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        n = len(weight)
        ans = 0
        i = n -1
        while i >= 1:
            if weight[i-1] > weight[i]:
                ans += 1
                i -=1
            i-= 1
        return ans

