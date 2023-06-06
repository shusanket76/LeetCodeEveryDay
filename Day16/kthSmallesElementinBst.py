# link="https://leetcode.com/problems/kth-smallest-element-in-a-bst/"
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(root):
            element=[]
            if not root:
                return
            if root.left:
                element = element+inorder(root.left)
            element.append(root.val)
            if root.right:
                element = element+inorder(root.right)
            return element
        a = inorder(root)
        return a[k-1] 