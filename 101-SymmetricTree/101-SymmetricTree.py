# Last updated: 6/8/2025, 11:55:19 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def is_mirror(n1 , n2):
            if not n1 and not n2 :
                return True
            if (not n1 and n2) or (not n2 and n1):
                return False
            if n1.val != n2.val:
                return False
            return (is_mirror(n1.left,n2.right) and is_mirror(n1.right,n2.left))
        
        return is_mirror(root.left , root.right)