# import collections
# from typing import List

# class Solution:
    
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         rows, cols = len(matrix), len(matrix[0])
#         first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
#         first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

#         # Use first row and column to mark zeros
#         for i in range(1, rows):
#             for j in range(1, cols):
#                 if matrix[i][j] == 0:
#                     matrix[i][0] = 0
#                     matrix[0][j] = 0

#         # Zero out cells based on markers in first row/column
#         for i in range(1, rows):
#             for j in range(1, cols):
#                 if matrix[i][0] == 0 or matrix[0][j] == 0:
#                     matrix[i][j] = 0

#         # Handle the first row and first column separately
#         if first_row_has_zero:
#             for j in range(cols):
#                 matrix[0][j] = 0

#         if first_col_has_zero:
#             for i in range(rows):
#                 matrix[i][0] = 0


# if __name__ == "__main__":
#     matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
#     solution = Solution()
#     solution.setZeroes(matrix)
#     print(matrix)


from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        # Step 1: Check if first row or column has a zero
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

        print("Initial Matrix:")
        for row in matrix:
            print(row)
        print()

        print(f"First row has zero: {first_row_has_zero}")
        print(f"First column has zero: {first_col_has_zero}")
        print()

        # Step 2: Use first row and column to mark zeros
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    print(f"matrix = {matrix[i][j]}")
                    matrix[i][0] = 0
                    matrix[0][j] = 0


        print("Matrix after marking phase:")
        for row in matrix:
            print(row)
        print()

        # Step 3: Zero out inner cells based on markers
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    print(f"matrix[i][0] = {matrix[i][0]} & matrix[0][j] = {matrix[0][j]}")
                    matrix[i][j] = 0

        print("Matrix after zeroing inner cells:")
        for row in matrix:
            print(row)
        print()

        # Step 4: Handle first row
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0

        # Step 5: Handle first column
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0

        print("Final matrix after zeroing first row and column:")
        for row in matrix:
            print(row)
        print()
        

if __name__ == "__main__":
    # matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    solution = Solution()
    solution.setZeroes(matrix)
    print("Final matrix (outside function):")
    print(matrix)

matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]