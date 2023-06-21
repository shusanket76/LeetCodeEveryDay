# link = "https://leetcode.com/problems/clone-graph/"

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        oldtoNew = {}

        def dfs(node):
            if node in oldtoNew:
                return oldtoNew[node]
            copy = Node(node.val)
            oldtoNew[node]=copy
            for x in node.neighbors:
                copy.neighbors.append(dfs(x))
            return copy
        return dfs(node) if node else None
       