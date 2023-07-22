class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        path=set()
        res=[]

        def dfs(x,y):
            if (x,y) not in path and x>=0 and x<len(matrix) and y>=0 and y<len(matrix[0]):
                path.add((x,y))
                res.append(matrix[x][y])
                print(y,matrix[x][y])
                if ((x-1,y) not in path) and (y-1<0 or (x,y-1) in path):
                    dfs(x-1,y)
                
                dfs(x,y+1)
                dfs(x+1,y)
                dfs(x,y-1)
                dfs(x-1,y)
            return res
        
        dfs(0,0)
        return res