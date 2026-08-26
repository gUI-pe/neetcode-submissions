class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            for j in range(9):
                #dot check
                if board[i][j] == ".":
                    continue
                #duplicate check
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[i // 3, j // 3]:
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
              #add to 3x3 squares 
                squares[i // 3,j // 3].add(board[i][j])
        return True
        #for linhas in board:
        #    print(linhas)

        #print(rows)
        #print(cols)
        #print(squares) 