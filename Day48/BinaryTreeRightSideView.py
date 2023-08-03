from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            qlen=len(queue)
            first = True
            for x in range(qlen):
                node = queue.popleft()

                if node:
                    if first:
                        res.append(node.val)
                        first = False
                    if node.right:
                    
                        queue.append(node.right)
                    if node.left:
                        queue.append(node.left)
        return res

        