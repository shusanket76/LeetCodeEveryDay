class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        path=set()
        def dfs(x,y):
            if x>=0 and y>=0 and x<len(board) and y<len(board[0]) and (x,y) not in path and board[x][y]=="O":
                board[x][y]="S"
                path.add((x,y))
                dfs(x+1,y)
                dfs(x-1,y)
                dfs(x,y+1)
                dfs(x,y-1)
            
        for x in range(len(board)):
            if board[x][0]=="O":
                dfs(x,0)
            if board[x][len(board[0])-1]=="O":
                dfs(x,len(board[0])-1)
        for y in range(len(board[0])):
            if board[0][y]=="O":
                dfs(0,y)
            if board[len(board)-1][y]=="O":
                dfs(len(board)-1,y)
        
        for a in range(len(board)):
            for b in range(len(board[0])):
                if board[a][b]=="O":
                    board[a][b]='X'
        for c in range(len(board)):
            for d in range(len(board[0])):
                if board[c][d]=="S":
                    board[c][d]="O"