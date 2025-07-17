# Last updated: 7/17/2025, 1:40:07 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        s = ""
        if not root:
            return ""
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if curr == None:
                s += "#,"
            else:
                s += str(curr.val) + ","
                q.append(curr.left)
                q.append(curr.right)
        return s
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        q = deque()
        token = data.split(',')
        root_val = int(token.pop(0))
        root = TreeNode(root_val)
        q.append(root)
        while q:
            curr = q.popleft()
            left_val = token.pop(0)
            if left_val != '#':
                left_node = TreeNode(int(left_val))
                curr.left = left_node
                q.append(left_node)
            right_val = token.pop(0)
            if right_val != '#':
                right_node = TreeNode(int(right_val))
                curr.right = right_node
                q.append(right_node)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))