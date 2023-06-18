# link = "https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/submissions/"

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        hasset = set()
        
        def countconnected(graph,node):
            if node not in hasset:
                hasset.add(node)
                for x in graph[node]:
                    countconnected(graph,x)
                return True
            
            else:
                return False
        if len(edges)!=0:
            graph = self.adjancenyList(edges)
            count =0 
            
            for x in graph:
                
                if countconnected(graph,x) is True:
                    print(x)
                    count=count+1
            print(graph)
            while n >len(graph.items()):
                count=count+1
                n=n-1
            return count
        return n


    def adjancenyList(self,edges):
        hasgra={}
        for x in edges:
            
            if x[0] in hasgra:
                hasgra[x[0]].append(x[1])
            else:
                hasgra[x[0]]=[x[1]]
            if x[1] in hasgra:
                hasgra[x[1]].append(x[0])
            else:
                hasgra[x[1]]=[x[0]]
        return hasgra



