# link="https://leetcode.com/problems/invert-binary-tree/submissions/965256007/"
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        temp= root.left
        root.left=root.right
        root.right=temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root