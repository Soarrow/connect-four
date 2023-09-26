class Board:
    """
    A Connect Four board represented as a 2D matrix (6x7).
    0 represents an empty cell, 1 for Player 1, and 2 for Player 2.
    """

    # Generate a connect four board represented by a 2D matric (6x7)
    _rows = 6
    _cols = 7

    # constructor
    def __init__(self):
        self._board = [[0 for col in range(self._cols)] for row in range(self._rows)]
        self._board.append([i for i in range(7)])

    # print the string representation of the board
    def __str__(self):
        # for row in range(len(self._board)):
        #     print(self._board[row])

        board_str = ""
        for row in self._board:
            row_str = " ".join(map(str, row))
            board_str += f"{row_str}\n"
        
        return board_str