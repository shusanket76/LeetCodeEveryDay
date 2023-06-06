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
        
