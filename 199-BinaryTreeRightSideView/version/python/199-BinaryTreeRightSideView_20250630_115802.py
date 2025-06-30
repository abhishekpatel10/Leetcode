# Last updated: 6/30/2025, 11:58:02 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        node = defaultdict()
        q = deque()
        q.append((root,0))
        while q:
            temp,row = q.popleft()
            node[row] = temp.val
            if temp.left:
                q.append((temp.left,row+1))
            if temp.right:
                q.append((temp.right,row+1))
        for key,value in sorted(node.items()):
            ans.append(value)
        return ans