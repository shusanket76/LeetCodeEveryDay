def exist(board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROWS,COLUMNS = len(board), len(board[0])
        path = set()
        
        def dfs(r,c,i):
            if i==len(word):
                return True
            if(r<0 or c<0 or r>=ROWS or c>=COLUMNS or word[i]!=board[r][c] or (r,c) in path):
                return False
            
            path.add((r,c))
            res = (dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1))
            path.remove((r,c))
            return res
        for r in range(ROWS):
            for c in range(COLUMNS):
                if dfs(r,c,0):
                    return True
        return False
board = [["a","b"],["c","d"]]
word="cdba"
a = exist(board,word)
print(a)