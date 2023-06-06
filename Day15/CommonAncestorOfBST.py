# link = "https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/965283217/"
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # root = root
        while root:
            if root.val<p.val and root.val<q.val:
                root=root.right
            elif root.val>p.val and root.val>q.val:
                root = root.left
            else:
                return root