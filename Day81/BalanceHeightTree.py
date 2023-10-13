# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        res = [True]

        def dfs(l,r, root):
  

            if not root:
                return 0
            if not root.right and not root.left:
                return 1
            l+=dfs(0,0, root.left)
            if not res[0]:
                return False
            r+=dfs(0,0,root.right)
            if (r-l)>1 or(l-r)>1:
                res[0] = False
            return max(l,r)+1
        dfs(0,0,root)
        return res[0]

            
            
            