class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i]
            row_values = list(filter(lambda x: x!=".", row))
            
            if len(row_values) != len(set(row_values)):
                print("row_values : ", row_values, set(row_values))
                return False
            
            col = [board[0][i], board[1][i], board[2][i], 
                   board[3][i], board[4][i], board[5][i], 
                   board[6][i], board[7][i], board[8][i], 
                  ]
            col_values = list(filter(lambda x: x!=".", col))
            if len(col_values) != len(set(col_values)):
                print("col_values : ", col_values, set(col_values))
                return False
            
            sub = [board[i//3*3+0][i%3*3], board[i//3*3+0][i%3*3+1], board[i//3*3+0][i%3*3+2],
                   board[i//3*3+1][i%3*3], board[i//3*3+1][i%3*3+1], board[i//3*3+1][i%3*3+2],
                   board[i//3*3+2][i%3*3], board[i//3*3+2][i%3*3+1], board[i//3*3+2][i%3*3+2],
                  ]
            sub_values = list(filter(lambda x: x!=".", sub))
            if len(sub_values) != len(set(sub_values)):
                print("sub_values : ", sub_values, set(sub_values))
                return False
            
        return True

    
board=[[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]