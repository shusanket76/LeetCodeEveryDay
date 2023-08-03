# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root) -> int:
        res =[0]

        def dfs(root, maxval):
            if not root:
                return 
            if root.val>=maxval:
                    res[0]+=1
            if root.left:
                maxval = max(root.val, maxval)
                dfs(root.left, maxval)
            if root.right:
                maxval=max(root.val, maxval)
                dfs(root.right, maxval)

            
            
        dfs(root, root.val)
        return res[0]