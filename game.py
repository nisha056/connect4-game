from board import Board
from player import Player
from game_logic import GameLogic

class ConnectFourGame:
    def __init__(self, columns: int, rows: int, players_signs: tuple):
        self.board = Board(columns, rows)
        self.players = [Player(sign) for sign in players_signs]
        self.current_player = None
        self.game_logic = GameLogic()

    def start_game(self):
        self.current_player = self.players[0]
        while True:
            if self.play_turn():
                break

    def play_turn(self):
        self.board.display_board()
        column = self.current_player.get_player_input(self.board.columns, self.board.board)
        roww = self.board.update_board(column, self.current_player.sign)

        if self.game_logic.check_winner(self.board.board, roww, column, self.current_player.sign):
            self.board.display_board()
            print(f"Congratulations, {self.current_player.sign}! You won!")
            return True
        elif self.game_logic.is_draw(self.board.board):
            self.board.display_board()
            print("It's a draw!")
            return True

        self.current_player = Player.switch_player(self.current_player, self.players)
        return False


if __name__ == '__main__':
    game = ConnectFourGame(7, 6, ('X', 'O'))
    game.start_game()