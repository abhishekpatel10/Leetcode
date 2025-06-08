# Last updated: 6/8/2025, 11:54:04 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def balanced(p,q):
            if not p and not q :
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            if p.val != q.val:
                return False
            
            return balanced(p.left,q.left) and balanced(p.right , q.right)
        
        def has_subTree(root):
            if not root:
                return False
            
            if balanced(root,subRoot):
                return True
            
            return has_subTree(root.left) or has_subTree(root.right)
        return has_subTree(root)