class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        board = [[board[y][x] for x in range(3)] for y in range(3)]
        cnt_O, cnt_O_line, cnt_X, cnt_X_line = 0, 0, 0, 0
        
        if board[0][0] + board[1][1] + board[2][2] == "XXX":
            cnt_X_line += 1
            
        if board[0][0] + board[1][1] + board[2][2] == "OOO":
            cnt_O_line += 1
            
        if board[0][2] + board[1][1] + board[2][0] == "XXX":
            cnt_X_line += 1
            
        if board[0][2] + board[1][1] + board[2][0] == "OOO":
            cnt_O_line += 1
        
        for i in range(3):
            if board[0][i] + board[1][i] + board[2][i] == "XXX":
                cnt_X_line += 1
            elif board[0][i] + board[1][i] + board[2][i] == "OOO":
                cnt_O_line += 1
                
            if board[i][0] + board[i][1] + board[i][2] == "XXX":
                cnt_X_line += 1
            elif board[i][0] + board[i][1] + board[i][2] == "OOO":
                cnt_O_line += 1
        
        print(f"O line: {cnt_O_line}, X line: {cnt_X_line}")
        
        for y in range(3):
            for x in range(3):
                if board[y][x] == 'O':
                    cnt_O += 1
                elif board[y][x] == 'X':
                    cnt_X += 1
        
        print(f"O: {cnt_O}, X: {cnt_X}")
        
        
        if cnt_X - cnt_O == 0 and cnt_X_line == 0 and cnt_O_line < 2:
            return True
        
        elif cnt_X - cnt_O == 1 and cnt_X_line < 2 and cnt_O_line == 0:
            return True
        
        elif cnt_X == 5 and cnt_O == 4 and cnt_X_line == 2: # 한방에 X두줄 완성하는 경우
            return True
        
        else:
            return False