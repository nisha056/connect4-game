from board import Board
import random
class Player:
    def __init__(self, sign: str):
        self.sign = sign

    @staticmethod
    # switch between players
    def switch_player(current_player, players):
        # return the player who is not the current player
        return next(player for player in players if player != current_player)

    # get valid user input for the column
    def get_player_input(self, columns: int, board) -> int:
        while True:
            try:
                # prompt the user for input and convert it to an integer
                column = int(input(f"{self.sign}, please input column number: "))
                # column = random.randint(0, 6)

                # check if the entered column is within the valid range
                if 0 <= column < columns:
                    # Check if the selected column is already full
                    if any(board[row][column] == Board.EMPTY_CELL for row in range(len(board))):
                        return column
                    else:
                        print("Column is full. Please choose another column.")
                else:
                    print("Invalid column. Please choose a valid column.")
            except ValueError:
                print("Invalid input. Please enter a number.")
