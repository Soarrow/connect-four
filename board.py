import pygame
import sys

class Board:
    """
    A Connect Four board represented as a 2D matrix (6x7).
    0 represents an empty cell, 1 for Player 1, and 2 for Player 2.
    """

    # Generate a connect four board represented by a 2D matric (6x7)
    _rows = 6
    _cols = 7
    _game_end = False
    _player_number = 1

    # Using pygame to generate the game
    _squaresize = 100 # what we define a square to be in px?s
    _width = _cols * _squaresize
    _height = (_rows + 1) * _squaresize
    _size = (_width, _height) # used to define the size of the screen

    _radius = int(_squaresize/2 - 5)

    _BLUE = (0,0,255)
    _BLACK = (0,0,0)

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

        # initialise pygame
        pygame.init()

        # Create 
        screen = pygame.display.set_mode(self._size)

        self.draw_board(screen)
        pygame.display.update()

        while not self._game_end:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                


                # if event.type == pygame.MOUSEBUTTONDOWN:


            # self.player_make_move()
            # # printing the board
            # print(self)
            # print("")
        
        # print(f"Congratulations player {self._player_number}! You won")
    
    # This function is called when it's a player's turn to make a move
    def player_make_move(self):

        print(f"Player {self._player_number}'s turn")
        user_picked_column = int(input("Please enter the column of where you want to place your coin: "))
        valid = self.valid_move(user_picked_column)

        # if the move is valid place the block
        if valid:
            # print("that was a valid move")
            next_empty_row = self.find_next_valid_row(user_picked_column)
            self.make_move(next_empty_row, user_picked_column)
            
        else:
            print("That was not a valid move please try again")
        
        if self.win_condition():
                self._game_end = True;

        if self._player_number == 1 and self._game_end is not True:
            self._player_number = 2
        elif self._player_number == 2 and self._game_end is not True:
            self._player_number = 1


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

    # This funciton places the piece that a palyer wants to make
    def make_move(self, next_empty_row, user_picked_column):
        # Change the player piece based on whose turn it is
        player_piece = "C" if self._player_number == 1 else "X"

        self._board[next_empty_row][user_picked_column] = player_piece

    def win_condition(self):
        # up to the third column you can have a winning horizontal move ... past the third column you can no longer win horizontally
        player_piece = "C" if self._player_number == 1 else "X"

        # Check horizontal
        # for each row check the next four columns to see if there is a winning combination of player pieces
        # then move on to the next column in the same row and check the next four spaces to see ifo there is a winning combination
        # for col in range(self._cols - 3):
        #     for row in range(self._rows):
        #         if self._board[row][col] == player_piece and self._board[row][col + 1] == player_piece and self._board[row][col + 2] == player_piece and self._board[row][col + 3] == player_piece:
        #             return True

        # Another way to check the horizontal win conditions
        for row in range(self._rows):
            for col in range(self._cols - 3):
                if self._board[row][col] == player_piece and self._board[row][col + 1] == player_piece and self._board[row][col + 2] == player_piece and self._board[row][col + 3] == player_piece:
                    return True

        # Check vertical winning conditions
        # for each column check the next four rows to see iof there is a winning combination of pieces
        # then move onto the next row in the same col and check the next four pieces etc.
        for col in range(self._cols):
            for row in range(self._rows - 3):
                if self._board[row][col] == player_piece and self._board[row + 1][col] == player_piece and self._board[row + 2][col] == player_piece and self._board[row + 3][col] == player_piece:
                    return True

        # Check diagonal win conditions have to do it both ways: positively slopped and negatively slopped
        # check diagonals first cause that is easier lmao
        for row in range(self._rows - 3):
            for col in range(self._cols - 3):
                if self._board[row][col] == player_piece and self._board[row + 1][col + 1] == player_piece and self._board[row + 2][col + 2] == player_piece and self._board[row + 3][col + 3] == player_piece:
                    return True

        # Check the positive diagonals for possible wins
        for row in range(self._rows - 1, self._rows - 4, -1):
            for col in range(self._cols - 3):
                if self._board[row][col] == player_piece and self._board[row - 1][col + 1] == player_piece and self._board[row - 2][col + 2] == player_piece and self._board[row - 3][col + 3] == player_piece:
                    return True

    def draw_board(self, screen):
        for row in range(self._rows):
            for col in range(self._cols):
                pygame.draw.rect(screen, self._BLUE, (col*self._squaresize, row*self._squaresize+self._squaresize, self._squaresize, self._squaresize))
                pygame.draw.circle(screen, self._BLACK, (col*self._squaresize + self._squaresize/2, row*self._squaresize+self._squaresize+self._squaresize/2), self._radius)