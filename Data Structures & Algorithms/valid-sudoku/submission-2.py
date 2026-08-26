class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for i in range(9):
            for j in range(9):
                #dot check
                if board[i][j] == ".":
                    continue
                #duplicate check
                value = int(board[i][j]) - 1
                if (1 << value) & rows[i] or (1 << value) & cols[j] or (1 << value) & squares[(i // 3 * 3) + (j // 3)]:
                    return False

                rows[i] |= (1 << value)
                cols[j] |= (1 << value)
              #add to 3x3 squares 
                squares[(i // 3) * 3 + (j // 3)] |= (1 << value)
        return True