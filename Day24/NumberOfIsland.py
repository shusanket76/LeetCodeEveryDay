# link = "https://leetcode.com/problems/number-of-islands/description/"

from collections import deque
class Solution(object):
    def numIslands(self,grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        hasset =  set()
        def explore(grid,a,b,lengtha,lengthb):
            d=0
            if a<lengtha and  b<lengthb:
                stack = deque()
                stack.append((a,b))
                while stack:
                    node = stack.pop()
                    a=node[0]
                    b=node[1]
                    if node not in hasset and node[0]<lengtha and node[1]<lengthb and 0<=node[0] and 0<=node[1]  and grid[a][b]=="1":
                        d=1
                        hasset.add(node)
                        stack.append((a,b-1))
                        stack.append((a,b+1))
                        stack.append((a-1,b))
                        stack.append((a+1,b))
            return d    
        count = 0
        for x in range(len(grid)):
            lenght_x = len(grid)
            for y in range(len(grid[x])):
                length_y = len(grid[x])
                if grid[x][y]=="1":
                    if explore(grid, x,y,lenght_x,length_y) ==1:
                        count = count+1
        return count
            