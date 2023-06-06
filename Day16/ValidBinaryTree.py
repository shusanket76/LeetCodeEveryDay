# link="https://leetcode.com/problems/validate-binary-search-tree/submissions/965302478/"

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def valid(root,left,right):
            if not root:
                return True
            if not(root.val>left and root.val<right):
                return False
            return (valid(root.left,left,root.val) and valid(root.right, root.val,right))
        return valid(root,float("-inf"), float("inf")) 