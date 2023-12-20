class Board:
    EMPTY_CELL = ' '

    # initializes a new game board
    def __init__(self, columns: int, rows: int):
        self.columns = columns
        self.rows = rows
        # initialize the board with empty cells
        self.board = [[Board.EMPTY_CELL] * columns for _ in range(rows)]
        # self.board = [[str((c, r)) for c in range(columns)] for r in range(rows)]

    # display the current board state
    def display_board(self):
        for row in self.board:
            print("|", " | ".join(row), "|")
            print("-" * (4 * self.columns + 1))
        print(" " + "   ".join(map(str, range(self.columns))))

    # update the board with a player's move
    def update_board(self, column: int, player_sign: str):
        # iterate through the rows of specified column, starting from the bottom
        for row in range(self.rows - 1, -1, -1):
            # check if the current cell is empty
            if self.board[row][column] == Board.EMPTY_CELL:
                # update the cell with the player's sign
                self.board[row][column] = player_sign
                return row

