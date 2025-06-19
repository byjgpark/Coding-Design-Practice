from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        print("Starting Sudoku validation...")
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                print(f"Inspecting cell (row={r}, col={c}): '{val}'")

                if val == ".":
                    print("  - Empty cell, skipping.")
                    continue

                # Check for duplicates
                if val in rows[r]:
                    print(f"  ! Duplicate '{val}' found in row {r}")
                    return False
                if val in cols[c]:
                    print(f"  ! Duplicate '{val}' found in column {c}")
                    return False
                if val in squares[(r // 3, c // 3)]:
                    print(f"  ! Duplicate '{val}' found in 3x3 square { (r//3, c//3) }")
                    return False

                # No duplicates; record the value
                rows[r].add(val)
                cols[c].add(val)
                squares[(r // 3, c // 3)].add(val)
                print(f"  + Added '{val}' to row {r}, col {c}, square { (r//3, c//3) }")
                # Print current state of the row, column, and square
                print(f"    rows[{r}] = {rows[r]}")
                print(f"    cols[{c}] = {cols[c]}")
                print(f"    squares[{(r//3, c//3)}] = {squares[(r//3, c//3)]}")

        print("No duplicates found. Sudoku is valid.")
        print("cols =", cols, "rows", rows, "squares", squares)
        return True

if __name__ == "__main__":
    sample_board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    solution = Solution()
    result = solution.isValidSudoku(sample_board)
    
    print(f"Result: {result}")

