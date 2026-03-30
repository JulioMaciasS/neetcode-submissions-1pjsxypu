class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate 3 x 3 squares
        for row in range(0, 9):
            for col in range(0, 9):
                # check for column clashes
                # check for items in theleft side
                currentCell = board[row][col]
                if currentCell == ".":
                        continue
               
                for i in range(0, 9):
                    if i == col:
                        continue
               
                    if board[row][i] == currentCell:
                        return False

                for i in range(0, 9):
                    if i == row:
                        continue
                    if board[i][col] == currentCell:
                        return False


                colRef = col // 3 * 3
                rowRef = row // 3 * 3
                for r in range(rowRef, rowRef + 3):
                    for c in range (colRef, colRef + 3):
                        currentItem = board[r][c]
                        if currentItem == "." or (r == row and c == col):
                            continue
                        elif currentItem == currentCell:
                            return False
                            
        return True