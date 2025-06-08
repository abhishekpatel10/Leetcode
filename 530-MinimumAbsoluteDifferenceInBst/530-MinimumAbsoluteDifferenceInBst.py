# Last updated: 6/8/2025, 11:54:11 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ans = [float('inf')]
        prev = [None]
        def dfs(root):
            if root is None:
                return 
            dfs(root.left)
            if prev[0] is not None:
                ans[0] = min(ans[0] , root.val - prev[0])
            prev[0] = root.val
            dfs(root.right)
        dfs(root)
        return ans[0]
            
