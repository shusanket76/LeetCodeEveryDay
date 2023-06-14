# link = "https://leetcode.com/explore/interview/card/microsoft/31/trees-and-graphs/197/"
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque()
        queue.append(root)
        res=[]
        left=False
        while queue:
            ans=[]
            a=0
            qlen = len(queue)
            while a<qlen:
                node = queue.popleft()
                if node:
                    ans.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                    
                a=a+1
            if len(ans)!=0:
                print(ans)
                res.append(reversed(ans) if len(res)%2 else ans)
        
        return res