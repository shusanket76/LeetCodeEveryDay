# def maxAreaOfIsland( grid) -> int:
#         res = float("-inf")

#         path=set()
#         def dfs(x,y,path,count):
#             if (x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and (x,y) not in path and grid[x][y]==1):
#                 path.add((x,y))
#                 count+=1
#                 count= dfs(x-1,y,path, count)
#                 count =dfs(x+1,y,path, count)
#                 count = dfs(x,y+1,path, count)
#                 count = dfs(x,y-1,path, count)
#             return count
            
            
        
#         for x in range(len(grid)):
#             for y in range(len(grid[0])):
#                 if grid[x][y]==1:
#                     count = 0
#                     res = max(res, dfs(x,y,path, count))
#         return int(res)
    
# a=[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# b = maxAreaOfIsland(a)
# print(b)


print(max(-9,0))