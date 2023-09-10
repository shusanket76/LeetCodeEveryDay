# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:

        def dfs(root, tar):
            if not root:
                return False
            tar+=root.val
            if tar==targetSum:
                if not root.right and not root.left:
                    return True
            return (dfs(root.left, tar) or dfs(root.right, tar))
            

        return (dfs(root, 0))        