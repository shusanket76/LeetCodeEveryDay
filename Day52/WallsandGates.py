from collections import deque
class Solution:
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        visit = set()
        row = len(rooms)
        col = len(rooms[0])
        q = deque()
        for r in range(row):
            for c in range(col):
                if rooms[r][c]==0:
                    q.append([r,c])
                    visit.add((r,c))
                    
        def addRoom(r,c):
            if r<0 or r==row or c<0 or c==col or (r,c) in visit or rooms[r][c]==-1:
                return 
            visit.add((r,c))
            q.append([r,c])

        dist = 0
        while q:
            for i in range(len(q)):
                r,c =q.popleft()
                rooms[r][c] = dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist+=1