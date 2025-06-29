from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9
        
        # Helper function to format integer as 9-bit binary string
        def format_bitmask(bits):
            return format(bits, '09b')  # Formats to 9 digits with leading zeros
        
        print("Starting Sudoku validation...")
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    print(f"  Cell ({r},{c}): empty, skipping")
                    continue
                    
                digit = board[r][c]
                val = int(digit) - 1
                pos = 1 << val
                square_index = (r // 3) * 3 + (c // 3)
                
                print(f"\nProcessing cell ({r},{c}): digit = {digit}")
                print(f"  Row {r} bitmask: {format_bitmask(rows[r])}")
                print(f"  Col {c} bitmask: {format_bitmask(cols[c])}")
                print(f"  Square {square_index} bitmask: {format_bitmask(squares[square_index])}")
                
                # Check for duplicates
                if rows[r] & pos:
                    print(f"  !!! Duplicate {digit} found in row {r}")
                    return False
                if cols[c] & pos:
                    print(f"  !!! Duplicate {digit} found in column {c}")
                    return False
                if squares[square_index] & pos:
                    print(f"  !!! Duplicate {digit} found in square {square_index}")
                    return False
                
                # Update bitmasks
                rows[r] |= pos
                cols[c] |= pos
                squares[square_index] |= pos
                
                print(f"  Updated row {r} bitmask: {format_bitmask(rows[r])}")
                print(f"  Updated col {c} bitmask: {format_bitmask(cols[c])}")
                print(f"  Updated square {square_index} bitmask: {format_bitmask(squares[square_index])}")
        
        print("\nValidation complete: board is valid!")
        return True
    
    if __name__ == "__main__":  
        solution = Solution()
        board = [
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
        solution.isValidSudoku(board)
