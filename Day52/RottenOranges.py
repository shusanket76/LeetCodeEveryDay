from collections import deque

class Solution:
    def orangesRotting(self, grid) -> int:
        queue = deque()
        time,fresh = 0,0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1:
                    fresh+=1
                if grid[x][y]==2:
                    queue.append([x,y])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while queue and fresh >0:
            for ab in range(len(queue)):
                r,c = queue.popleft()
                for cd in directions:
                    row,col = r+cd[0], c+cd[1]
                    if row>=0 and col>=0 and row<len(grid) and col<len(grid[0]) and grid[row][col]==1:
                        queue.append([row,col])
                        grid[row][col]=2
                        fresh-=1
                    else:
                        continue
            time+=1
        return time if fresh==0 else -1

