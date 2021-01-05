import logging
from itertools import count
from config import SQUARE_SIZE, CURRENT_TIME
from config.moves import moves, default_positions

class PieceCoordinates:
    """Contains the coordinates of each square in the game. The size of each square is 50 and that's 
    what the calculations here are based on."""

    zero_to_fifty = []
    count_for_zero_to_fifty = count(start=SQUARE_SIZE*0, step=1)
    for _ in range(51):
        zero_to_fifty.append(next(count_for_zero_to_fifty))

    fifty_to_onehundred = []
    count_for_fifty_to_onehundred = count(start=SQUARE_SIZE*1, step=1)
    for _ in range(50, 101):
        fifty_to_onehundred.append(next(count_for_fifty_to_onehundred))

    onehundred_to_onefifty = []
    count_for_onehundred_to_onefifty = count(start=SQUARE_SIZE*2, step=1)
    for _ in range(100, 151):
        onehundred_to_onefifty.append(next(count_for_onehundred_to_onefifty))

    onefifty_to_twohundred = []
    count_for_onefifty_to_twohundred = count(start=SQUARE_SIZE*3, step=1)
    for _ in range(150, 201):
        onefifty_to_twohundred.append(next(count_for_onefifty_to_twohundred))

    twohundred_to_twofifty = []
    count_for_twohundred_to_twofifty = count(start=SQUARE_SIZE*4, step=1)
    for _ in range(200, 251):
        twohundred_to_twofifty.append(next(count_for_twohundred_to_twofifty))

    twofifty_to_threehundred = []
    count_for_twofifty_to_threehundred = count(start=SQUARE_SIZE*5, step=1)
    for _ in range(250, 301):
        twofifty_to_threehundred.append(next(count_for_twofifty_to_threehundred))

    threehundred_to_threefifty = []
    count_for_threehundred_to_threefifty = count(start=SQUARE_SIZE*6, step=1)
    for _ in range(300, 351):
        threehundred_to_threefifty.append(next(count_for_threehundred_to_threefifty))

    threefifty_to_fourhundred = []
    count_for_threefifty_to_fourhundred = count(start=SQUARE_SIZE*7, step=1)
    for _ in range(350, 401):
        threefifty_to_fourhundred.append(next(count_for_threefifty_to_fourhundred))

    @classmethod
    def check_piece_coordinates(cls, x_coords, y_coords):
        """Takes in the X and Y coordinates of the mouseclick as an argument. These are provided by
        the event.pos in the game loop, which is in app.py. This function will check the entire chess 
        board, row by row, for which square was clicked."""
        def check_rows():
            # ROW 8
            if x_coords in (cls.zero_to_fifty) and y_coords in (cls.zero_to_fifty):
                return 'a8'
            elif x_coords in (cls.fifty_to_onehundred) and y_coords in (cls.zero_to_fifty):
                return 'b8'
            elif x_coords in (cls.onehundred_to_onefifty) and y_coords in (cls.zero_to_fifty):
                return 'c8'
            elif x_coords in (cls.onefifty_to_twohundred) and y_coords in (cls.zero_to_fifty):
                return 'd8'
            elif x_coords in (cls.twohundred_to_twofifty) and y_coords in (cls.zero_to_fifty):
                return 'e8'
            elif x_coords in (cls.twofifty_to_threehundred) and y_coords in (cls.zero_to_fifty):
                return 'f8'
            elif x_coords in (cls.threehundred_to_threefifty) and y_coords in (cls.zero_to_fifty):
                return 'g8'
            elif x_coords in (cls.threefifty_to_fourhundred) and y_coords in (cls.zero_to_fifty):
                return 'h8'

            # ROW 7
            if x_coords in (cls.zero_to_fifty) and y_coords in (cls.fifty_to_onehundred):
                return 'a7'
            elif x_coords in (cls.fifty_to_onehundred) and y_coords in (cls.fifty_to_onehundred):
                return 'b7'
            elif x_coords in (cls.onehundred_to_onefifty) and y_coords in (cls.fifty_to_onehundred):
                return 'c7'
            elif x_coords in (cls.onefifty_to_twohundred) and y_coords in (cls.fifty_to_onehundred):
                return 'd7'
            elif x_coords in (cls.twohundred_to_twofifty) and y_coords in (cls.fifty_to_onehundred):
                return 'e7'
            elif x_coords in (cls.twofifty_to_threehundred) and y_coords in (cls.fifty_to_onehundred):
                return 'f7'
            elif x_coords in (cls.threehundred_to_threefifty) and y_coords in (cls.fifty_to_onehundred):
                return 'g7'
            elif x_coords in (cls.threefifty_to_fourhundred) and y_coords in (cls.fifty_to_onehundred):
                return 'h7'
        
            # ROW 6
            if x_coords in (cls.zero_to_fifty) and y_coords in (cls.onehundred_to_onefifty):
                return 'a6'
            elif x_coords in (cls.fifty_to_onehundred) and y_coords in (cls.onehundred_to_onefifty):
                return 'b6'
            elif x_coords in (cls.onehundred_to_onefifty) and y_coords in (cls.onehundred_to_onefifty):
                return 'c6'
            elif x_coords in (cls.onefifty_to_twohundred) and y_coords in (cls.onehundred_to_onefifty):
                return 'd6'
            elif x_coords in (cls.twohundred_to_twofifty) and y_coords in (cls.onehundred_to_onefifty):
                return 'e6'
            elif x_coords in (cls.twofifty_to_threehundred) and y_coords in (cls.onehundred_to_onefifty):
                return 'f6'
            elif x_coords in (cls.threehundred_to_threefifty) and y_coords in (cls.onehundred_to_onefifty):
                return 'g6'
            elif x_coords in (cls.threefifty_to_fourhundred) and y_coords in (cls.onehundred_to_onefifty):
                return 'h6'

            # ROW 5
            if x_coords in (cls.zero_to_fifty) and y_coords in (cls.onefifty_to_twohundred):
                return 'a5'
            elif x_coords in (cls.fifty_to_onehundred) and y_coords in (cls.onefifty_to_twohundred):
                return 'b5'
            elif x_coords in (cls.onehundred_to_onefifty) and y_coords in (cls.onefifty_to_twohundred):
                return 'c5'
            elif x_coords in (cls.onefifty_to_twohundred) and y_coords in (cls.onefifty_to_twohundred):
                return 'd5'
            elif x_coords in (cls.twohundred_to_twofifty) and y_coords in (cls.onefifty_to_twohundred):
                return 'e5'
            elif x_coords in (cls.twofifty_to_threehundred) and y_coords in (cls.onefifty_to_twohundred):
                return 'f5'
            elif x_coords in (cls.threehundred_to_threefifty) and y_coords in (cls.onefifty_to_twohundred):
                return 'g5'
            elif x_coords in (cls.threefifty_to_fourhundred) and y_coords in (cls.onefifty_to_twohundred):
                return 'h5'

            # ROW 4
            if x_coords in (cls.zero_to_fifty) and y_coords in (cls.twohundred_to_twofifty):
                return 'a4'
            elif x_coords in (cls.fifty_to_onehundred) and y_coords in (cls.twohundred_to_twofifty):
                return 'b4'
            elif x_coords in (cls.onehundred_to_onefifty) and y_coords in (cls.twohundred_to_twofifty):
                return 'c4'
            elif x_coords in (cls.onefifty_to_twohundred) and y_coords in (cls.twohundred_to_twofifty):
                return 'd4'
            elif x_coords in (cls.twohundred_to_twofifty) and y_coords in (cls.twohundred_to_twofifty):
                return 'e4'
            elif x_coords in (cls.twofifty_to_threehundred) and y_coords in (cls.twohundred_to_twofifty):
                return 'f4'
            elif x_coords in (cls.threehundred_to_threefifty) and y_coords in (cls.twohundred_to_twofifty):
                return 'g4'
            elif x_coords in (cls.threefifty_to_fourhundred) and y_coords in (cls.twohundred_to_twofifty):
                return 'h4'

            # ROW 3
            if x_coords in (cls.zero_to_fifty) and y_coords in (cls.twofifty_to_threehundred):
                return 'a3'
            elif x_coords in (cls.fifty_to_onehundred) and y_coords in (cls.twofifty_to_threehundred):
                return 'b3'
            elif x_coords in (cls.onehundred_to_onefifty) and y_coords in (cls.twofifty_to_threehundred):
                return 'c3'
            elif x_coords in (cls.onefifty_to_twohundred) and y_coords in (cls.twofifty_to_threehundred):
                return 'd3'
            elif x_coords in (cls.twohundred_to_twofifty) and y_coords in (cls.twofifty_to_threehundred):
                return 'e3'
            elif x_coords in (cls.twofifty_to_threehundred) and y_coords in (cls.twofifty_to_threehundred):
                return 'f3'
            elif x_coords in (cls.threehundred_to_threefifty) and y_coords in (cls.twofifty_to_threehundred):
                return 'g3'
            elif x_coords in (cls.threefifty_to_fourhundred) and y_coords in (cls.twofifty_to_threehundred):
                return 'h3'
            
            # ROW 2
            if x_coords in (cls.zero_to_fifty) and y_coords in (cls.threehundred_to_threefifty):
                return 'a2'
            elif x_coords in (cls.fifty_to_onehundred) and y_coords in (cls.threehundred_to_threefifty):
                return 'b2'
            elif x_coords in (cls.onehundred_to_onefifty) and y_coords in (cls.threehundred_to_threefifty):
                return 'c2'
            elif x_coords in (cls.onefifty_to_twohundred) and y_coords in (cls.threehundred_to_threefifty):
                return 'd2'
            elif x_coords in (cls.twohundred_to_twofifty) and y_coords in (cls.threehundred_to_threefifty):
                return 'e2'
            elif x_coords in (cls.twofifty_to_threehundred) and y_coords in (cls.threehundred_to_threefifty):
                return 'f2'
            elif x_coords in (cls.threehundred_to_threefifty) and y_coords in (cls.threehundred_to_threefifty):
                return 'g2'
            elif x_coords in (cls.threefifty_to_fourhundred) and y_coords in (cls.threehundred_to_threefifty):
                return 'h2'

            # ROW 1
            if x_coords in (cls.zero_to_fifty) and y_coords in (cls.threefifty_to_fourhundred):
                return 'a1'
            elif x_coords in (cls.fifty_to_onehundred) and y_coords in (cls.threefifty_to_fourhundred):
                return 'b1'
            elif x_coords in (cls.onehundred_to_onefifty) and y_coords in (cls.threefifty_to_fourhundred):
                return 'c1'
            elif x_coords in (cls.onefifty_to_twohundred) and y_coords in (cls.threefifty_to_fourhundred):
                return 'd1'
            elif x_coords in (cls.twohundred_to_twofifty) and y_coords in (cls.threefifty_to_fourhundred):
                return 'e1'
            elif x_coords in (cls.twofifty_to_threehundred) and y_coords in (cls.threefifty_to_fourhundred):
                return 'f1'
            elif x_coords in (cls.threehundred_to_threefifty) and y_coords in (cls.threefifty_to_fourhundred):
                return 'g1'
            elif x_coords in (cls.threefifty_to_fourhundred) and y_coords in (cls.threefifty_to_fourhundred):
                return 'h1'

        returned_address = check_rows()

        if returned_address == None:
            logging.error(f"{CURRENT_TIME} - The program failed to check the selected piece's coordinates.")

        """Start from row 8. If the address is not found there, search in row 7. If not found there, then move to row 6. Continue
        down all the way to row 1. The address SHOULD be found by now."""

        return returned_address

black_dp = default_positions[0]["Black"]
white_dp = default_positions[1]["White"]

class BlackCoordinates():
    # Gives you X/Y Coordinates like (300, 300), etc.
    BLACK_KING_COORDINATES = moves[(black_dp["king"])]
    BLACK_QUEEN_COORDINATES = moves[(black_dp["queen"])]

    BLACK_RIGHT_ROOK_COORDINATES = moves[(black_dp["right_rook"])]
    BLACK_LEFT_ROOK_COORDINATES = moves[(black_dp["left_rook"])]
    BLACK_RIGHT_KNIGHT_COORDINATES = moves[(black_dp["right_knight"])]
    BLACK_LEFT_KNIGHT_COORDINATES = moves[(black_dp["left_knight"])]
    BLACK_RIGHT_BISHOP_COORDINATES = moves[(black_dp["right_bishop"])]
    BLACK_LEFT_BISHOP_COORDINATES = moves[(black_dp["left_bishop"])]

    BLACK_PAWN_A7_COORDINATES = moves[(black_dp["pawn1"])]
    BLACK_PAWN_B7_COORDINATES = moves[(black_dp["pawn2"])]
    BLACK_PAWN_C7_COORDINATES = moves[(black_dp["pawn3"])]
    BLACK_PAWN_D7_COORDINATES = moves[(black_dp["pawn4"])]
    BLACK_PAWN_E7_COORDINATES = moves[(black_dp["pawn5"])]
    BLACK_PAWN_F7_COORDINATES = moves[(black_dp["pawn6"])]
    BLACK_PAWN_G7_COORDINATES = moves[(black_dp["pawn7"])]
    BLACK_PAWN_H7_COORDINATES = moves[(black_dp["pawn8"])]

class WhiteCoordinates():
    # Gives you X/Y Coordinates like (300, 300), etc.
    WHITE_KING_COORDINATES = moves[(white_dp["king"])]
    WHITE_QUEEN_COORDINATES = moves[(white_dp["queen"])]

    WHITE_RIGHT_ROOK_COORDINATES = moves[(white_dp["right_rook"])]
    WHITE_LEFT_ROOK_COORDINATES = moves[(white_dp["left_rook"])]
    WHITE_RIGHT_KNIGHT_COORDINATES = moves[(white_dp["right_knight"])]
    WHITE_LEFT_KNIGHT_COORDINATES = moves[(white_dp["left_knight"])]
    WHITE_RIGHT_BISHOP_COORDINATES = moves[(white_dp["right_bishop"])]
    WHITE_LEFT_BISHOP_COORDINATES = moves[(white_dp["left_bishop"])]

    WHITE_PAWN_A7_COORDINATES = moves[(white_dp["pawn1"])]
    WHITE_PAWN_B7_COORDINATES = moves[(white_dp["pawn2"])]
    WHITE_PAWN_C7_COORDINATES = moves[(white_dp["pawn3"])]
    WHITE_PAWN_D7_COORDINATES = moves[(white_dp["pawn4"])]
    WHITE_PAWN_E7_COORDINATES = moves[(white_dp["pawn5"])]
    WHITE_PAWN_F7_COORDINATES = moves[(white_dp["pawn6"])]
    WHITE_PAWN_G7_COORDINATES = moves[(white_dp["pawn7"])]
    WHITE_PAWN_H7_COORDINATES = moves[(white_dp["pawn8"])]

ALL_PIECE_COORDINATES = [
        BlackCoordinates.BLACK_KING_COORDINATES, BlackCoordinates.BLACK_QUEEN_COORDINATES, 
        BlackCoordinates.BLACK_RIGHT_ROOK_COORDINATES, BlackCoordinates.BLACK_LEFT_ROOK_COORDINATES, 
        BlackCoordinates.BLACK_RIGHT_KNIGHT_COORDINATES, BlackCoordinates.BLACK_LEFT_KNIGHT_COORDINATES, 
        BlackCoordinates.BLACK_RIGHT_BISHOP_COORDINATES, BlackCoordinates.BLACK_LEFT_BISHOP_COORDINATES, 
        BlackCoordinates.BLACK_PAWN_A7_COORDINATES, BlackCoordinates.BLACK_PAWN_B7_COORDINATES, 
        BlackCoordinates.BLACK_PAWN_C7_COORDINATES, BlackCoordinates.BLACK_PAWN_D7_COORDINATES, 
        BlackCoordinates.BLACK_PAWN_E7_COORDINATES, BlackCoordinates.BLACK_PAWN_F7_COORDINATES, 
        BlackCoordinates.BLACK_PAWN_G7_COORDINATES, BlackCoordinates.BLACK_PAWN_H7_COORDINATES,


        WhiteCoordinates.WHITE_KING_COORDINATES, WhiteCoordinates.WHITE_QUEEN_COORDINATES, 
        WhiteCoordinates.WHITE_RIGHT_ROOK_COORDINATES, WhiteCoordinates.WHITE_LEFT_ROOK_COORDINATES, 
        WhiteCoordinates.WHITE_RIGHT_KNIGHT_COORDINATES, WhiteCoordinates.WHITE_LEFT_KNIGHT_COORDINATES, 
        WhiteCoordinates.WHITE_RIGHT_BISHOP_COORDINATES, WhiteCoordinates.WHITE_LEFT_BISHOP_COORDINATES, 
        WhiteCoordinates.WHITE_PAWN_A7_COORDINATES, WhiteCoordinates.WHITE_PAWN_B7_COORDINATES, 
        WhiteCoordinates.WHITE_PAWN_C7_COORDINATES, WhiteCoordinates.WHITE_PAWN_D7_COORDINATES, 
        WhiteCoordinates.WHITE_PAWN_E7_COORDINATES, WhiteCoordinates.WHITE_PAWN_F7_COORDINATES, 
        WhiteCoordinates.WHITE_PAWN_G7_COORDINATES, WhiteCoordinates.WHITE_PAWN_H7_COORDINATES]

class BlackPosition():
    # Gives you addresses like 'd4', 'h2', 'e7', etc.
    BLACK_KING_POSITION = (black_dp["king"])
    BLACK_QUEEN_POSITION = (black_dp["queen"])

    BLACK_RIGHT_ROOK_POSITION = (black_dp["right_rook"])
    BLACK_LEFT_ROOK_POSITION = (black_dp["left_rook"])
    BLACK_RIGHT_KNIGHT_POSITION = (black_dp["right_knight"])
    BLACK_LEFT_KNIGHT_POSITION = (black_dp["left_knight"])
    BLACK_RIGHT_BISHOP_POSITION = (black_dp["right_bishop"])
    BLACK_LEFT_BISHOP_POSITION = (black_dp["left_bishop"])

    BLACK_PAWN_A7_POSITION = (black_dp["pawn1"])
    BLACK_PAWN_B7_POSITION = (black_dp["pawn2"])
    BLACK_PAWN_C7_POSITION = (black_dp["pawn3"])
    BLACK_PAWN_D7_POSITION = (black_dp["pawn4"])
    BLACK_PAWN_E7_POSITION = (black_dp["pawn5"])
    BLACK_PAWN_F7_POSITION = (black_dp["pawn6"])
    BLACK_PAWN_G7_POSITION = (black_dp["pawn7"])
    BLACK_PAWN_H7_POSITION = (black_dp["pawn8"])

class WhitePosition():
    # Gives you addresses like 'd4', 'h2', 'e7', etc.
    WHITE_KING_POSITION = (white_dp["king"])
    WHITE_QUEEN_POSITION = (white_dp["queen"])

    WHITE_RIGHT_ROOK_POSITION = (white_dp["right_rook"])
    WHITE_LEFT_ROOK_POSITION = (white_dp["left_rook"])
    WHITE_RIGHT_KNIGHT_POSITION = (white_dp["right_knight"])
    WHITE_LEFT_KNIGHT_POSITION = (white_dp["left_knight"])
    WHITE_RIGHT_BISHOP_POSITION = (white_dp["right_bishop"])
    WHITE_LEFT_BISHOP_POSITION = (white_dp["left_bishop"])

    WHITE_PAWN_A7_POSITION = (white_dp["pawn1"])
    WHITE_PAWN_B7_POSITION = (white_dp["pawn2"])
    WHITE_PAWN_C7_POSITION = (white_dp["pawn3"])
    WHITE_PAWN_D7_POSITION = (white_dp["pawn4"])
    WHITE_PAWN_E7_POSITION = (white_dp["pawn5"])
    WHITE_PAWN_F7_POSITION = (white_dp["pawn6"])
    WHITE_PAWN_G7_POSITION = (white_dp["pawn7"])
    WHITE_PAWN_H7_POSITION = (white_dp["pawn8"])

    print(WHITE_KING_POSITION)

ALL_PIECE_POSITIONS = [
        BlackPosition.BLACK_KING_POSITION, BlackPosition.BLACK_QUEEN_POSITION, 
        BlackPosition.BLACK_RIGHT_ROOK_POSITION, BlackPosition.BLACK_LEFT_ROOK_POSITION, 
        BlackPosition.BLACK_RIGHT_KNIGHT_POSITION, BlackPosition.BLACK_LEFT_KNIGHT_POSITION, 
        BlackPosition.BLACK_RIGHT_BISHOP_POSITION, BlackPosition.BLACK_LEFT_BISHOP_POSITION, 
        BlackPosition.BLACK_PAWN_A7_POSITION, BlackPosition.BLACK_PAWN_B7_POSITION, 
        BlackPosition.BLACK_PAWN_C7_POSITION, BlackPosition.BLACK_PAWN_D7_POSITION, 
        BlackPosition.BLACK_PAWN_E7_POSITION, BlackPosition.BLACK_PAWN_F7_POSITION, 
        BlackPosition.BLACK_PAWN_G7_POSITION, BlackPosition.BLACK_PAWN_H7_POSITION,


        WhitePosition.WHITE_KING_POSITION, WhitePosition.WHITE_QUEEN_POSITION, 
        WhitePosition.WHITE_RIGHT_ROOK_POSITION, WhitePosition.WHITE_LEFT_ROOK_POSITION, 
        WhitePosition.WHITE_RIGHT_KNIGHT_POSITION, WhitePosition.WHITE_LEFT_KNIGHT_POSITION, 
        WhitePosition.WHITE_RIGHT_BISHOP_POSITION, WhitePosition.WHITE_LEFT_BISHOP_POSITION, 
        WhitePosition.WHITE_PAWN_A7_POSITION, WhitePosition.WHITE_PAWN_B7_POSITION, 
        WhitePosition.WHITE_PAWN_C7_POSITION, WhitePosition.WHITE_PAWN_D7_POSITION, 
        WhitePosition.WHITE_PAWN_E7_POSITION, WhitePosition.WHITE_PAWN_F7_POSITION, 
        WhitePosition.WHITE_PAWN_G7_POSITION, WhitePosition.WHITE_PAWN_H7_POSITION]