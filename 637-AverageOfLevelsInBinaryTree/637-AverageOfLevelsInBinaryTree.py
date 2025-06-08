# Last updated: 6/8/2025, 11:54:00 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return 0
        queue = deque([root])
        ans = []
        while queue:
            level, count = 0, len(queue)
            for i in range(len(queue)):
                curr = queue.popleft()
                level += curr.val
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            ans.append(level/count)
        return ans