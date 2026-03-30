class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in range(9):
            seen = set()
            for col in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)

        # Check columns
        for col in range(9):
            seen = set()
            for row in range(9):
                value = board[row][col]
                if value == ".":
                    continue
                if value in seen:
                    return False
                seen.add(value)

        # Check 3x3 boxes
        for box in range(9):
            seen = set()
            start_row = (box // 3) * 3
            start_col = (box % 3) * 3

            for r in range(start_row, start_row + 3):
                for c in range(start_col, start_col + 3):
                    value = board[r][c]
                    if value == ".":
                        continue
                    if value in seen:
                        return False
                    seen.add(value)

        return True