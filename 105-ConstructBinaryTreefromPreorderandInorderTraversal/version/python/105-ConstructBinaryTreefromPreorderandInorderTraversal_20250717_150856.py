# Last updated: 7/17/2025, 3:08:56 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {val:idx for idx,val in enumerate(inorder)}
        return self._buildTree(preorder,0,len(preorder) - 1, inorder,0,len(inorder) - 1,inMap)
    def _buildTree(self,preorder,ps,pe,inorder,ins,ine,inMap):
        if ps > pe or ins > ine:
            return
        root = TreeNode(preorder[ps])
        idx = inMap[root.val]
        numsLeft = idx - ins
        root.left = self._buildTree(preorder,ps+1,ps+numsLeft,inorder,ins,idx-1,inMap)
        root.right = self._buildTree(preorder,ps+numsLeft+1,pe,inorder,idx+1,ine,inMap)
        return root