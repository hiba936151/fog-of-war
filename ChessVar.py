# Contains the methods containing information on each type of chess piece, functionality, and the actual board.

class ChessPiece:
    """
    A class that holds the color information for each chess piece
    """
    def __init__(self, color):
        self._color = color

    def get_color(self):
        """
        returns the color of the piece
        """
        return self._color

class Pawn(ChessPiece):
    """
    Contains the information and valid moves for a pawn
    """
    def __init__(self, color):
        super().__init__(color)

    def list_valid_moves(self, origin, board):
        """
        Takes in the square that the piece is moving from and returns a list of valid moves
        """

        possible_moves = []
        row, col = origin

        if self._color == "white":
            # Move forward if the square is empty
            if row - 1 >= 0 and board[row - 1][col] == " ":
                possible_moves.append((row - 1, col))

            # Move forward two spaces if starting position is clear
            if row == 6 and board[row - 1][col] == " " and board[row - 2][col] == " ":
                possible_moves.append((row - 2, col))

            # Diagonal captures
            if row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1].islower():
                possible_moves.append((row - 1, col - 1))
            if row - 1 >= 0 and col + 1 < 8 and board[row - 1][col + 1].islower():
                possible_moves.append((row - 1, col + 1))

        elif self._color == "black":
            # Move forward if the square is empty
            if row + 1 < 8 and board[row + 1][col] == " ":
                possible_moves.append((row + 1, col))

            # Move forward two spaces if starting position is clear
            if row == 1 and board[row + 1][col] == " " and board[row + 2][col] == " ":
                possible_moves.append((row + 2, col))

            # Diagonal captures
            if row + 1 < 8 and col - 1 >= 0 and board[row + 1][col - 1].isupper():
                possible_moves.append((row + 1, col - 1))
            if row + 1 < 8 and col + 1 < 8 and board[row + 1][col + 1].isupper():
                possible_moves.append((row + 1, col + 1))

        return possible_moves

class Bishop(ChessPiece):
    """
    Contains the information and valid moves for a bishop
    """
    def __init__(self, color):
        super().__init__(color)

    def list_valid_moves(self, origin, board):
        """
        Takes in the square that the piece is moving from and returns a list of valid moves
        """
        possible_moves = []

        # moving toward upper left
        row_idx = origin[0]
        col_idx = origin[1]
        while row_idx > 0 and col_idx > 0:
            row_idx -= 1
            col_idx -= 1
            next_space = board[row_idx][col_idx]
            next_space_index = (row_idx, col_idx)
            if next_space == " ":
                possible_moves.append(next_space_index)
            elif self._color == "white" and next_space.islower():
                possible_moves.append(next_space_index)
                break
            elif self._color == "black" and next_space.isupper():
                possible_moves.append(next_space_index)
                break
            else:
                # breaks the loop if it encounters a like-colored piece
                break

        # moving toward upper right
        row_idx = origin[0]
        col_idx = origin[1]
        while row_idx > 0 and col_idx < 7:
            row_idx -= 1
            col_idx += 1
            next_space = board[row_idx][col_idx]
            next_space_index = (row_idx, col_idx)
            if next_space == " ":
                possible_moves.append(next_space_index)
            elif self._color == "white" and next_space.islower():
                possible_moves.append(next_space_index)
                break
            elif self._color == "black" and next_space.isupper():
                possible_moves.append(next_space_index)
                break
            else:
                # breaks the loop if it encounters a like-colored piece
                break

        # moving toward lower left
        row_idx = origin[0]
        col_idx = origin[1]
        while row_idx < 7 and col_idx > 0:
            row_idx += 1
            col_idx -= 1
            next_space = board[row_idx][col_idx]
            next_space_index = (row_idx, col_idx)
            if next_space == " ":
                possible_moves.append(next_space_index)
            elif self._color == "white" and next_space.islower():
                possible_moves.append(next_space_index)
                break
            elif self._color == "black" and next_space.isupper():
                possible_moves.append(next_space_index)
                break
            else:
                # breaks the loop if it encounters a like-colored piece
                break

        # moving toward lower right
        row_idx = origin[0]
        col_idx = origin[1]
        while row_idx < 7 and col_idx < 7:
            row_idx += 1
            col_idx += 1
            next_space = board[row_idx][col_idx]
            next_space_index = (row_idx, col_idx)
            if next_space == " ":
                possible_moves.append(next_space_index)
            elif self._color == "white" and next_space.islower():
                possible_moves.append(next_space_index)
                break
            elif self._color == "black" and next_space.isupper():
                possible_moves.append(next_space_index)
                break
            else:
                # breaks the loop if it encounters a like-colored piece
                break

        return possible_moves

class Rook(ChessPiece):
    """
    Contains the information and valid moves for a rook
    """
    def __init__(self, color):
        super().__init__(color)

    def list_valid_moves(self, origin, board):
        """
        Takes in the square that the piece is moving from and returns a list of valid moves
        """
        possible_moves = []

        # Moving upwards
        row_idx, col_idx = origin
        while row_idx > 0:
            row_idx -= 1
            next_space = board[row_idx][col_idx]
            next_space_index = (row_idx, col_idx)
            if next_space == " ":
                possible_moves.append(next_space_index)
            elif (self._color == "white" and next_space.islower()) or (self._color == "black" and next_space.isupper()):
                possible_moves.append(next_space_index)
                break
            else:
                break

        # Moving downwards
        row_idx, col_idx = origin
        while row_idx < 7:
            row_idx += 1
            next_space = board[row_idx][col_idx]
            next_space_index = (row_idx, col_idx)
            if next_space == " ":
                possible_moves.append(next_space_index)
            elif (self._color == "white" and next_space.islower()) or (self._color == "black" and next_space.isupper()):
                possible_moves.append(next_space_index)
                break
            else:
                break

        # Moving left
        row_idx, col_idx = origin
        while col_idx > 0:
            col_idx -= 1
            next_space = board[row_idx][col_idx]
            next_space_index = (row_idx, col_idx)
            if next_space == " ":
                possible_moves.append(next_space_index)
            elif (self._color == "white" and next_space.islower()) or (self._color == "black" and next_space.isupper()):
                possible_moves.append(next_space_index)
                break
            else:
                break

        # Moving right
        row_idx, col_idx = origin
        while col_idx < 7:
            col_idx += 1
            next_space = board[row_idx][col_idx]
            next_space_index = (row_idx, col_idx)
            if next_space == " ":
                possible_moves.append(next_space_index)
            elif (self._color == "white" and next_space.islower()) or (self._color == "black" and next_space.isupper()):
                possible_moves.append(next_space_index)
                break
            else:
                break

        return possible_moves

class Queen(ChessPiece):
    """
    Contains the information and valid moves for a queen
    """
    def __init__(self, color):
        super().__init__(color)

    def list_valid_moves(self, origin, board):
        """
        Takes in the square that the piece is moving from and returns a list of valid moves
        """
        possible_moves = []

        # copies over possible moves of a rook
        rook = Rook("white" if self._color == "white" else "black")
        rook_style_moves = rook.list_valid_moves(origin, board)

        # copies over possible moves of a bishop
        bishop = Bishop("white" if self._color == "white" else "black")
        bishop_style_moves = bishop.list_valid_moves(origin, board)

        # adds them to the list of possible moves for a queen
        for element in rook_style_moves:
            possible_moves.append(element)

        for element in bishop_style_moves:
            possible_moves.append(element)

        return possible_moves

class Knight(ChessPiece):
    """
    Contains the information and valid moves for a knight.
    """
    def __init__(self, color):
        super().__init__(color)

    def list_valid_moves(self, origin, board):
        """
        Takes in the square that the piece is moving from and returns a list of valid moves.
        """
        possible_moves = []
        row_idx, col_idx = origin
        # All possible "L" shaped moves for a knight
        move_combinations = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

        for change in move_combinations:
            new_row = row_idx + change[0]
            new_col = col_idx + change[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                next_space = board[new_row][new_col]
                if next_space == " " or (self._color == "white" and next_space.islower()) or (self._color == "black" and next_space.isupper()):
                    possible_moves.append((new_row, new_col))

        return possible_moves

class King(ChessPiece):
    """
    Contains the information and valid moves for a king.
    """
    def __init__(self, color):
        super().__init__(color)

    def list_valid_moves(self, origin, board):
        """
        Takes in the square that the piece is moving from and returns a list of valid moves.
        """
        possible_moves = []
        row_idx, col_idx = origin
        # All possible directions for the king (1 square in any direction)
        move_combinations = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for change in move_combinations:
            new_row = row_idx + change[0]
            new_col = col_idx + change[1]
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                next_space = board[new_row][new_col]
                if next_space == " " or (self._color == "white" and next_space.islower()) or (self._color == "black" and next_space.isupper()):
                    possible_moves.append((new_row, new_col))

        return possible_moves

class ChessVar:
    """ implements an abstract board game based on a chess variant known as Fog of War chess"""
    def __init__(self):
        self._game_state = "UNFINISHED"
        # lowercase are black pieces, uppercase are white
        self._board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self._turn = "white"
        # initializes the number of turns to 0
        self._num_turns = 0

    def get_game_state(self):
        """
        Returns the game state (i.e., in progress, or which color won)
        """
        return self._game_state

    def get_board(self, perspective):
        """
        Returns the board based on the given user's perspective
        """
        board_copy = [row[:] for row in self._board]
        list_of_moves = self.set_visibility(perspective)

        if perspective == "white":
            # Return board from white player's perspective
            for row_index in range(len(board_copy)):
                row = board_copy[row_index]
                for column_index in range(len(row)):
                    piece = row[column_index]
                    if piece.islower() and (row_index, column_index) not in list_of_moves:
                        row[column_index] = "*"
            return board_copy

        elif perspective == "black":
            # Return board from black player's perspective
            for row_index in range(len(board_copy)):
                row = board_copy[row_index]
                for column_index in range(len(row)):
                    piece = row[column_index]
                    if piece.isupper() and (row_index, column_index) not in list_of_moves:
                        row[column_index] = "*"
            return board_copy

        elif perspective == "audience":
            return self._board

    def set_visibility(self, perspective):

        list_of_white_moves = []
        list_of_black_moves = []

        for row in range(8):
            for col in range(8):
                piece = self._board[row][col]
                origin = (row, col)

                if piece.lower() == "p":
                    pawn = Pawn("white" if piece.isupper() else "black")
                    if pawn.get_color() == "white":
                        valid_moves = pawn.list_valid_moves(origin, self._board)
                        for move in valid_moves:
                            list_of_white_moves.append(move)
                    else:
                        valid_moves = pawn.list_valid_moves(origin, self._board)
                        for move in valid_moves:
                            list_of_black_moves.append(move)

                if piece.lower() == "b":
                    bishop = Bishop("white" if piece.isupper() else "black")
                    if bishop.get_color() == "white":
                        valid_moves = bishop.list_valid_moves(origin, self._board)
                        for move in valid_moves:
                            list_of_white_moves.append(move)
                    else:
                        valid_moves = bishop.list_valid_moves(origin, self._board)
                        for move in valid_moves:
                            list_of_black_moves.append(move)

                if piece.lower() == "r":
                    rook = Rook("white" if piece.isupper() else "black")
                    if rook.get_color() == "white":
                        valid_moves = rook.list_valid_moves(origin, self._board)
                        for move in valid_moves:
                            list_of_white_moves.append(move)
                    else:
                        valid_moves = rook.list_valid_moves(origin, self._board)
                        for move in valid_moves:
                            list_of_black_moves.append(move)

                if piece.lower() == "q":
                    queen = Queen("white" if piece.isupper() else "black")
                    if queen.get_color() == "white":
                        valid_moves = queen.list_valid_moves(origin, self._board)
                        for move in valid_moves:
                            list_of_white_moves.append(move)
                    else:
                        valid_moves = queen.list_valid_moves(origin, self._board)
                        for move in valid_moves:
                            list_of_black_moves.append(move)

                if piece.lower() == "n":
                    knight = Knight("white" if piece.isupper() else "black")
                    if knight.get_color() == "white":
                        valid_moves = knight.list_valid_moves(origin, self._board)
                        for move in valid_moves:
                            list_of_white_moves.append(move)
                    else:
                        valid_moves = knight.list_valid_moves(origin, self._board)
                        for move in valid_moves:
                            list_of_black_moves.append(move)

                if piece.lower() == "k":
                    king = King("white" if piece.isupper() else "black")
                    if king.get_color() == "white":
                        valid_moves = king.list_valid_moves(origin, self._board)
                        for move in valid_moves:
                            list_of_white_moves.append(move)
                    else:
                        valid_moves = king.list_valid_moves(origin, self._board)
                        for move in valid_moves:
                            list_of_black_moves.append(move)

        if perspective == "white":
            return list_of_white_moves
        elif perspective == "black":
            return list_of_black_moves
        else:
            return

    def set_game_state(self, state):
        """
        Updates the game state; takes in the new state as an argument
        Game states are 'UNFINISHED', 'WHITE_WON', 'BLACK_WON'
        """
        self._game_state = state

    def translate_move(self, space_id):
        dict_to_index = {"a": 0,
                         "b": 1,
                         "c": 2,
                         "d": 3,
                         "e": 4,
                         "f": 5,
                         "g": 6,
                         "h": 7
                         }

        column = space_id[0]
        row = space_id[1]

        column = dict_to_index[column]
        row = 8 - int(row)

        return (row,column)

    def make_move(self, square_from, square_to):
        """
        If the square being moved from does not contain a piece belonging to the player whose turn it is,
        or if the indicated move is not legal, or if the game has already been won, returns False.
        Otherwise, makes the indicated move, removes any captured piece, updates the game state if necessary,
        updates whose turn it is, and returns True.
        """
        # translates the given spaces to indices on the array
        origin = self.translate_move(square_from)
        destination = self.translate_move(square_to)

        # gets the value of the pieces
        piece = self._board[origin[0]][origin[1]]
        destination_value = self._board[destination[0]][destination[1]]

        # if the space is empty, returns False
        if piece == " ":
            return False

        # if the player tries to move a piece that isn't theirs, returns False
        if (piece.isupper() and self._turn == "black") or (piece.islower() and self._turn == "white"):
            return False

        # if the game has already been won, returns false
        if self.get_game_state() != "UNFINISHED":
            return False

        # checks if a pawn move is valid
        if piece.lower() == "p":
            pawn = Pawn("white" if piece.isupper() else "black")
            list_of_valid_moves = pawn.list_valid_moves(origin, self._board)

        if piece.lower() == "b":
            bishop = Bishop("white" if piece.isupper() else "black")
            list_of_valid_moves = bishop.list_valid_moves(origin, self._board)

        if piece.lower() == "r":
            rook = Rook("white" if piece.isupper() else "black")
            list_of_valid_moves = rook.list_valid_moves(origin, self._board)

        if piece.lower() == "q":
            queen = Queen("white" if piece.isupper() else "black")
            list_of_valid_moves = queen.list_valid_moves(origin, self._board)

        if piece.lower() == "n":
            knight = Knight("white" if piece.isupper() else "black")
            list_of_valid_moves = knight.list_valid_moves(origin, self._board)

        if piece.lower() == "k":
            king = King("white" if piece.isupper() else "black")
            list_of_valid_moves = king.list_valid_moves(origin, self._board)

        # if the destination is in the list of valid moves for that piece, returns true
        if destination in list_of_valid_moves:
            move_is_valid = True
        else:
            move_is_valid = False

        # if the space trying to move to is the same color, can't move there
        if destination_value.isupper() and piece.isupper():
            move_is_valid = False
        if destination_value.islower() and piece.islower():
            move_is_valid = False

        if move_is_valid is True:
            # makes the move and updates the board. if the king is captured, updates the game state
            self._board[destination[0]][destination[1]] = self._board[origin[0]][origin[1]]
            self._board[origin[0]][origin[1]] = " "

            if destination_value == "K":
                self.set_game_state("WHITE_WON")
            elif destination_value == "k":
                self.set_game_state("BLACK_WON")

            # updates the turn
            self.track_turn()

            # returns True
            return True

        else:
            return False

    def track_turn(self):
        """
        Keeps track of which player's turn it is and updates self._turn after each valid move
        """
        # switches turn
        if self._turn == "white":
            self._turn = "black"
        else:
            self._turn = "white"
        self._num_turns += 1
