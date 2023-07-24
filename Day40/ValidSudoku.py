class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hascol = {}
        hasrow={}
        row = 0
        col = 0
        while row<len(board)-2:
            col=0
            while col<len(board[0])-2:
                uptorow = row+3
                uptocol = col+3
                samegrid = set()
                for a in range(row,uptorow):
                    for b in range(col,uptocol):
                        if board[a][b]==".":
                            continue
                        if board[a][b] in samegrid:
                            return False
                        else:
                            samegrid.add(board[a][b])
                        if a in hasrow:
                            if board[a][b] in hasrow[a]:
                                return False
                            else:
                                hasrow[a].add(board[a][b])

                        else:
                            hasrow[a] = set(board[a][b])
                        if b in hascol:
                            if board[a][b] in hascol[b]:
                                return False
                            else:
                                hascol[b].add(board[a][b])
                        else:
                            hascol[b] = set(board[a][b])
                        
                col+=3
            row+=3
        return True