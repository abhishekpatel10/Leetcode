# Last updated: 7/15/2025, 7:33:33 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        path = {}
        ans = []
        if not root:
            return []
        q = deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                curr_node = q.popleft()

                if curr_node.left:
                    path[curr_node.left.val] = curr_node
                    q.append(curr_node.left)
                if curr_node.right:
                    path[curr_node.right.val] = curr_node
                    q.append(curr_node.right)
        visited = {}
        q.append(target)
        while k > 0 and q:
            for _ in range(len(q)):
                top = q.popleft()
                visited[top.val] = 1

                if top.left and top.left.val not in visited:
                    q.append(top.left)
                if top.right and top.right.val not in visited:
                    q.append(top.right)
                if top.val in path and path[top.val].val not in visited:
                    q.append(path[top.val])
            k -=1
        while q:
            ans.append(q.popleft().val)
        return ans