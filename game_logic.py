from board import Board  

class GameLogic:
    TO_CONNECT = 4

    @staticmethod
    # checks if current move leads to win
    def check_winner(board, row, col, player_sign):
        #print(row, col)
        a=0
        b=0
        c= row
        d= col
        if row> col:
            a=row-col
        else:
            b=col-row
        while (c>0 and d<6):
            c-=1
            d+=1
        return (
            # check for winning sequence horizontally
            GameLogic.check_line(board[row], player_sign) or
            # check for winning sequence vertically
            GameLogic.check_line([board[i][col] for i in range(len(board))], player_sign) or
            # check for winning sequence in main diagonal
            GameLogic.check_line([board[c+i][d - i] for i in range(min(6-c, 7+d)) if c+1 <=6 or d-i >=0],player_sign) or
            #GameLogic.check_line([board[i][row + col - i] for i in range(max(0, (row+col) - 6), min(row + col, 6))],player_sign) or
            # check for winning sequence in secondary diagonal
            GameLogic.check_line([board[a+i][b+i] for i in
                                  range( min(6-a, 7-b)) if a+1 <= 6 or b+i <=7], player_sign) 
        
        )

    @staticmethod
    # checks if there is a winning sequence in the given line
    def check_line(line, player_sign):
        count = 0
        #print(line)
        for cell in line:
            if cell == player_sign:
                count += 1
                if count == GameLogic.TO_CONNECT:
                    
                    return True
            else:
                count = 0
        return False

    @staticmethod
    # checks if the game is a draw
    def is_draw(board):
        return all(cell != Board.EMPTY_CELL for row in board for cell in row)
