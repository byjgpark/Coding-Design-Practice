# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for row in range(9):
#             seen = set()
#             for i in range(9):
#                 if board[row][i] == ".": 
#                     continue
#                 if board[row][i] in seen:
#                     return False
#                 seen.add(board[row][i])
        
#         for col in range(9):
#             seen = set()
#             for i in range(9):
#                 if board[i][col] == ".":
#                     continue
#                 if board[i][col] in seen:
#                     return False
#                 seen.add(board[i][col])
            
#         for square in range(9):
#             seen = set()
#             for i in range(3):
#                 for j in range(3):
#                     row = (square//3) * 3 + i
#                     col = (square % 3) * 3 + j
#                     if board[row][col] == ".":
#                         continue
#                     if board[row][col] in seen:
#                         return False
#                     seen.add(board[row][col])
                    
#         return True
    
    
# First try
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
        
#         rows = len(board)
#         cols = len(board[0])

#         print("check row = ", rows, "col = ", cols)

#         #checking row 
#         for row in range(rows):
#             seen = set()
#             for i in range(9):
#                 # print("check row = ", row, " i = ", i)

#                 if board[row][i] == ".":
#                     continue
#                 if board[row][i] in seen:
#                     return False
#                 seen.add(board[row][i])

#         print("check row seen = ", seen)

#         #checking column
#         for col in range(cols):
#             seen = set()
#             for i in range(9):
#                 # print("check row = ", row, " i = ", i)
#                 if board[i][col] == ".":
#                     continue
#                 if board[i][col] in seen:
#                     return False
#                 seen.add(board[i][col])
        
#         print("check column seen = ", seen)

#         #checking sub-box
#         for box in range(9):
#             seen = set()
#             for i in range(rows):
#                 for j in range(cols):
#                     row = (box // 3) * 3 + i
#                     col = (box % 3) * 3 + j

#                     print("check row = ", row, " col = ", col)
#                     if board[row][col] == ".":
#                         continue
#                     if board[row][col] in seen:
#                         return False
#                     seen.add(board[row][col])

#         return True


# Second try
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = len(board)
        cols = len(board[0])

        print("check row = ", rows, "col = ", cols)

        #checking row 
        for row in range(rows):
            seen = set()
            for i in range(9):
                # print("check row = ", row, " i = ", i)

                if board[row][i] == ".":
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])

        print("check row seen = ", seen)

        #checking column
        for col in range(cols):
            seen = set()
            for i in range(9):
                # print("check row = ", row, " i = ", i)
                if board[i][col] == ".":
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        
        print("check column seen = ", seen)

        #checking sub-box
        for box in range(9):
            seen = set()
            for i in range(rows):
                for j in range(cols):
                    row = (box // 3) * 3 + i
                    col = (box % 3) * 3 + j

                    print("check row = ", row, " col = ", col)
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True

                    

                    
                    
    
    