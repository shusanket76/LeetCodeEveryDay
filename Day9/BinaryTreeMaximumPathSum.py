# link = "https://leetcode.com/problems/binary-tree-maximum-path-sum/description/"
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [root.val]

        def maxVal(root):
            if not root:
                return 0
            a = maxVal(root.left)
            b = maxVal(root.right)
            leftmax = max(a,0)
            rightMax = max(b,0)

            res[0] = max(res[0], root.val+leftmax+rightMax)
            return root.val+max(leftmax,rightMax)
        maxVal(root)
        return res[0]