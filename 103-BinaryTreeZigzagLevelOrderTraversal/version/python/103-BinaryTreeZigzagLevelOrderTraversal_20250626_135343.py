# Last updated: 6/26/2025, 1:53:43 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        q = deque()
        lefttoright = True
        q.append(root)
        while q :
            curr = [0] * len(q)
            n = len(q)
            for i in range(len(q)):
                curr_node = q.popleft()
                idx = i if lefttoright else n - i - 1
                curr[idx] = curr_node.val
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            lefttoright =not lefttoright
            ans.append(curr)
        return ans