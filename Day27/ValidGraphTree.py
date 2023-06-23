# link = "https://leetcode.com/problems/graph-valid-tree/"

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if not n:
            return False
        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        path=set()
        def dfs(i,prev):
            if i in path:
                return False
            path.add(i)
            for j in adj[i]:
                if j==prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        return dfs(0,-1) and len(path)==n
            


        