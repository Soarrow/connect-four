class Board:
    """
    A Connect Four board represented as a 2D matrix (6x7).
    0 represents an empty cell, 1 for Player 1, and 2 for Player 2.
    """

    # Generate a connect four board represented by a 2D matric (6x7)
    _rows = 6
    _cols = 7
    _turn = 0

    # constructor
    def __init__(self):
        self._board = [[0 for col in range(self._cols)] for row in range(self._rows)]

    # print the string representation of the board
    def __str__(self):
        board_str = ""
        for row in self._board:
            row_str = " ".join(map(str, row))
            board_str += f"{row_str}\n"
        
        # add the last coordinate display row
        board_str += " ".join(map(str, [i for i in range(len(self._board[0]))]))
        return board_str

    # Functions that determine game logic

    # This function starts the game
    def run_game(self):
        game_end = False
        while not game_end:
            # player one moves
            if self._turn % 2 == 0:
                print("Player 1's turn")
                user_picked_column = int(input("Please enter the column of where you want to place your coin: "))
                valid = self.valid_move(user_picked_column)

                # if the move is valid place the block
                if valid:
                    # print("that was a valid move")
                    next_empty_row = self.find_next_valid_row(user_picked_column)
                    self.make_move(next_empty_row, user_picked_column)
                else:
                    print("That was not a valid move please try again")
                    break
                self._turn += 1

            # Player two moves
            else:
                print("Player 2's turn")
                user_picked_column = int(input("Please enter the column of where you want to place your coin: "))
                valid = self.valid_move(user_picked_column)

                # if the move is valid place the block
                if valid:
                    # print("that was a valid move")
                    next_empty_row = self.find_next_valid_row(user_picked_column)
                    self.make_move(next_empty_row, user_picked_column)
                else:
                    print("That was not a valid move please try again")
                    break
                self._turn += 1

            
            # check if the game is over if not increment the turn variable
            # increment the turn
            # if win_condition():
            #     game_end = True;
            # else:
            #     self._turn += 1

            
            # printing the board?
            print(self)
            print("")
            # break;

    def valid_move(self, user_picked_column: int) -> bool:
        # check to see if the top row is empty, if so then it is a valid move
        if (self._board[0][user_picked_column] == 0):
            return True
        
        return False
    
    def find_next_valid_row(self, user_picked_column: int) -> int:
        # find the next empty row of the column picked

        for i in range(len(self._board)-1, -1, -1):
            if self._board[i][user_picked_column] == 0:
                return i

    def make_move(self, next_empty_row, user_picked_column):
        # Change the player piece based on whose turn it is
        player_piece = "C" if self._turn % 2 == 0 else "X"

        self._board[next_empty_row][user_picked_column] = player_piece

    # def win_condition(self):
        # implement win condition logic

        # THINGS that we need to check, once placed we need to see if there are 4 of the same colour adjacent to one another

        # search in a square around the area that you have just placed. If there is a colour of the same kind that becomes the new node and then you search again

        # if you are able to count 3 in a row then you have won the game ... once at a new node you cannot come back to the same level if you have left the previous level
        # this applies horizontally or vertically

    # 0,0 should be translated into 5,0