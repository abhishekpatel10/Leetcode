# Last updated: 8/31/2025, 1:37:56 PM
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ss = set(friends)
        ans = []
        for o in order:
            if o in ss:
                ans.append(o)
        return ans
        