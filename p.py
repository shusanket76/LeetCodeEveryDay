def exist(board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(x,y,i, path):
                
                if  x>=0 and y>=0 and x<len(board) and y<len(board[0]) and board[x][y]==word[i] and (x,y) not in path: 
                    path.add((x,y))
                    if i==len(word)-1:
                        return True
                    a = dfs(x+1,y,i+1,path)
                    b = dfs(x-1,y,i+1,path)
                    c = dfs(x,y+1,i+1,path)
                    d = dfs(x,y-1,i+1,path)
                    path.remove((x,y))
                    return (a or b or c or d)
                else:
                    return False

      


            
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y]==word[0]:
                    path=set()
                    if dfs(x,y,0,path) is True:
                        return True
        return False
a = exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")
print(a)