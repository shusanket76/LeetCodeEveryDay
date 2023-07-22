class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        tochange=set()
        def dfs(x,y,a,b,path):
        
            if x>=0 and y>=0 and x<len(matrix) and y<len(matrix[0]) and (x,y) not in path:
                path.add((x,y))
                if x==a or y==b:
                    matrix[x][y]=0
                    dfs(x+1,y,a,b, path)
                    dfs(x-1,y,a,b, path)
                    dfs(x,y+1,a,b, path)
                    dfs(x,y-1,a,b, path)

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y]==0:
                    tochange.add((x,y))

        for a in tochange:
            path=set()
            x=a[0]
            y=a[1]
            dfs(x,y,x,y,path)
        