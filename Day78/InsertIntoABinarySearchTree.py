# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root, val: int):

        def dfs(root, val):
            if not root:
                root = TreeNode(val)
                return root
            if root.val == val:
                return root
            if root.val<val:
                if root.right:
                    dfs(root.right, val)
                    return root
                else:
                    root.right = TreeNode(val)
                    return root
            else:
                if root.left:
                    dfs(root.left, val)
                    return root
                else:
                    root.left = TreeNode(val)
                    return root
        

        return dfs(root, val)
        