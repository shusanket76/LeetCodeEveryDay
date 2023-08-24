# link = 'https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/965258041/'
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        a=self.maxDepth(root.left)+1
        b = self.maxDepth(root.right)+1
        return max(a,b)
# ========================================================================================++++?\
# SOLUTION2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root) -> int:
        res = [0]
        def dfs(root, count):
            if root:
                res[0] = max(res[0], count)
                dfs(root.left, count+1)
                dfs(root.right, count+1)
        dfs(root, 1)
        return res[0]
        
