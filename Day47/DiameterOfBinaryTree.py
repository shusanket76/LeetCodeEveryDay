# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:

        res = [-2]
        def dfs(root):
            if not root:
                return -1
            if not root.left and not root.right:
                return 0
            left = dfs(root.left)+1
            right = dfs(root.right)+1
            res[0] = max(res[0], left+right)
            return max(left,right)
        
        dfs(root)
        if res[0]==-2:
            return 0
        return res[0]
