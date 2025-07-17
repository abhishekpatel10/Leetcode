# Last updated: 7/17/2025, 3:12:53 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inMap = {val:idx for idx,val in enumerate(inorder)}
        return self.__buildTree(inorder,0,len(inorder)-1,postorder,0,len(postorder)-1,inMap,)
    def __buildTree(self,inorder,ins,ine,postorder,pos,poe,inMap):
        if ins > ine or pos > poe:
            return
        root = TreeNode(postorder[poe])
        idx = inMap[root.val]
        numsLeft = idx - ins
        root.left = self.__buildTree(inorder,ins,idx-1,postorder,pos,pos+numsLeft-1,inMap)
        root.right = self.__buildTree(inorder,idx+1,ine,postorder,pos+numsLeft,poe-1,inMap)
        return root
