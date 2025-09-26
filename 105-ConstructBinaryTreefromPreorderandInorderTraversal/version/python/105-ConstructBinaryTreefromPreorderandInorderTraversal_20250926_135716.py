# Last updated: 9/26/2025, 1:57:16 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {val: idx for idx, val in enumerate(inorder)}
        return self._buildTree(inorder,0,len(inorder) - 1,preorder,0,len(preorder) - 1 , inMap)
    def _buildTree(self,inorder,ins,ine,preorder,ps,pe,inMap):
        if ins > ine or ps > pe:
            return None
        root = TreeNode(preorder[ps])
        idx = inMap[root.val]
        numLeft = idx - ins
        root.left =  self._buildTree(inorder,ins,idx-1,preorder,ps+1,ps+numLeft,inMap)
        root.right = self._buildTree(inorder,idx+1,ine,preorder,ps+numLeft+1,pe,inMap)
        return root

