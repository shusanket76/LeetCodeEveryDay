# link ="https://leetcode.com/problems/subtree-of-another-tree/"
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root,subRoot):
            return True
        a = self.isSubtree(root.left,subRoot)
        b = self.isSubtree(root.right,subRoot)
        return (a or b)
    def sameTree(self,s,t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val!=t.val:
            return False
        return (self.sameTree(s.left,t.left) and self.sameTree(s.right,t.right))
