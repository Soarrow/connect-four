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
        row_counter = len(self._board) - 2
        last_row = False
        for row in self._board:
            if not last_row:
                board_str += str(row_counter) + " "
            else:
                board_str += "  "
                
            row_str = " ".join(map(str, row))
            board_str += f"{row_str}\n"
            
            if row_counter >= 0:
                row_counter -= 1
            
            if row_counter < 0:
                last_row = True
        
        return board_str

    # Functions that determine game logic

    # This function starts the game
    def run_game(self):
        while True:
            user_coords = input("Please enter the coordinates of where you want to place your coin x,y: ")
            self.valid_move(user_coords)
            break;

    def valid_move(self, coordinates: str) -> bool:
        # coordinate cannot be out of bounds
        # there has to be a coin below it unless it's in the last row

        # first we need to break the coordinate into x and y coords
        x_coord = coordinates.split(",")[0]
        y_coord = coordinates.split(",")[1]

        # now we need some logic to validate the coordinates

