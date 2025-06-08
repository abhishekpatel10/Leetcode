# Last updated: 6/8/2025, 11:54:50 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        d = deque()
        d.append(root)
        while d:
            rightSide = None
            for i in range(len(d)):
                curr = d.popleft()
                if curr:
                    rightSide = curr
                    d.append(curr.left)
                    d.append(curr.right)
            if rightSide:
                ans.append(rightSide.val)
        return ans