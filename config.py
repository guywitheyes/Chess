import pygame
from itertools import count
from datetime import datetime
from database.moves import moves, default_positions
import logging

# TODO: Since so much code in this project (not just this file) is repetitive, we will later move it to a JSON file or something
# so that we can reduce the repetitive code. This will likely shorten our entire project's code by hundreds of lines. Let's do this
# after the project has been completed. I don't want to deal with cleaning the code until the project has made substantial progress.

BLACK_SQUARE = pygame.image.load('assets/black-square.png')
WHITE_SQUARE = pygame.image.load('assets/white-square.png')
SQUARE_SIZE = 50

(SCREEN_WIDTH, SCREEN_HEIGHT) = (400, 400)

CURRENT_DATE = str(datetime.today().date().__str__()) # Used mostly in logging messages.
CURRENT_TIME = str(datetime.now().time().__str__()) # Used mostly in logging messages.

class PieceImages:
    """Loads the PNG images of all Chess pieces icons."""
    
    #BLACK: ------------------------------------------------
    BLACK_KING = pygame.image.load('assets/pieces/bk.png')
    BLACK_KING = pygame.transform.scale(BLACK_KING, (50, 50))

    BLACK_QUEEN = pygame.image.load('assets/pieces/bq.png')
    BLACK_QUEEN = pygame.transform.scale(BLACK_QUEEN, (50, 50))

    BLACK_ROOK = pygame.image.load('assets/pieces/br.png')
    BLACK_ROOK = pygame.transform.scale(BLACK_ROOK, (50, 50))

    BLACK_KNIGHT = pygame.image.load('assets/pieces/bn.png')
    BLACK_KNIGHT = pygame.transform.scale(BLACK_KNIGHT, (50, 50))

    BLACK_BISHOP = pygame.image.load('assets/pieces/bb.png')
    BLACK_BISHOP = pygame.transform.scale(BLACK_BISHOP, (50, 50))

    BLACK_PAWN = pygame.image.load('assets/pieces/bp.png')
    BLACK_PAWN = pygame.transform.scale(BLACK_PAWN, (50, 50))
    
    #WHITE: ------------------------------------------------
    WHITE_KING = pygame.image.load('assets/pieces/wk.png')
    WHITE_KING = pygame.transform.scale(WHITE_KING, (50, 50))

    WHITE_QUEEN = pygame.image.load('assets/pieces/wq.png')
    WHITE_QUEEN = pygame.transform.scale(WHITE_QUEEN, (50, 50))

    WHITE_ROOK = pygame.image.load('assets/pieces/wr.png')
    WHITE_ROOK = pygame.transform.scale(WHITE_ROOK, (50, 50))
    
    WHITE_KNIGHT = pygame.image.load('assets/pieces/wn.png')
    WHITE_KNIGHT = pygame.transform.scale(WHITE_KNIGHT, (50, 50))

    WHITE_BISHOP = pygame.image.load('assets/pieces/wb.png')
    WHITE_BISHOP = pygame.transform.scale(WHITE_BISHOP, (50, 50))

    WHITE_PAWN = pygame.image.load('assets/pieces/wp.png')
    WHITE_PAWN = pygame.transform.scale(WHITE_PAWN, (50, 50))   

class ChessNotation:
    """Contains chess notation, addresses, and other similar things."""
    # TODO: Move this default_positions dictionary to a JSON database.
    # Contains the starting positions of both Black and White pieces.
    

class Position:
    black_dp = default_positions[0]["Black"]
    white_dp = default_positions[1]["White"]

    @classmethod
    def select_piece(cls, piece):
        pass

    @classmethod
    def move_piece(cls, piece, position):
            """OK, so this function works. There's only one issue and it has nothing to do with this function
            anyway. It is being caused by the Chessboard.__init__() method. Since it is in the game loop, it
            is being called continously. The piece is moved, but in the next iteration of the game loop, the
            coordinates of the piece are set back to default."""

            # Until you've built this function fully, here's how the pieces are actually moved: (in case you forget)
            piece = moves[position]

class BlackPosition(Position):
    BLACK_KING_POSITION = moves[(Position.black_dp["king"])]
    BLACK_QUEEN_POSITION = moves[(Position.black_dp["queen"])]

    BLACK_RIGHT_ROOK_POSITION = moves[(Position.black_dp["right_rook"])]
    BLACK_LEFT_ROOK_POSITION = moves[(Position.black_dp["left_rook"])]
    BLACK_RIGHT_KNIGHT_POSITION = moves[(Position.black_dp["right_knight"])]
    BLACK_LEFT_KNIGHT_POSITION = moves[(Position.black_dp["left_knight"])]
    BLACK_RIGHT_BISHOP_POSITION = moves[(Position.black_dp["right_bishop"])]
    BLACK_LEFT_BISHOP_POSITION = moves[(Position.black_dp["left_bishop"])]

    BLACK_PAWN_A7_POSITION = moves[(Position.black_dp["pawn1"])]
    BLACK_PAWN_B7_POSITION = moves[(Position.black_dp["pawn2"])]
    BLACK_PAWN_C7_POSITION = moves[(Position.black_dp["pawn3"])]
    BLACK_PAWN_D7_POSITION = moves[(Position.black_dp["pawn4"])]
    BLACK_PAWN_E7_POSITION = moves[(Position.black_dp["pawn5"])]
    BLACK_PAWN_F7_POSITION = moves[(Position.black_dp["pawn6"])]
    BLACK_PAWN_G7_POSITION = moves[(Position.black_dp["pawn7"])]
    BLACK_PAWN_H7_POSITION = moves[(Position.black_dp["pawn8"])]


    BLACK_PIECES_ALL_POSITIONS = [BLACK_KING_POSITION, BLACK_QUEEN_POSITION, BLACK_RIGHT_ROOK_POSITION, 
                                BLACK_LEFT_ROOK_POSITION, BLACK_RIGHT_KNIGHT_POSITION, 
                                BLACK_LEFT_KNIGHT_POSITION, BLACK_RIGHT_BISHOP_POSITION, 
                                BLACK_LEFT_BISHOP_POSITION, BLACK_PAWN_A7_POSITION,
                                BLACK_PAWN_B7_POSITION, BLACK_PAWN_C7_POSITION, BLACK_PAWN_D7_POSITION, 
                                BLACK_PAWN_E7_POSITION, BLACK_PAWN_F7_POSITION, BLACK_PAWN_G7_POSITION,
                                BLACK_PAWN_H7_POSITION]

# TODO: Add the POSITIONs for all the white pieces, including white pawns.
class WhitePosition(Position):
    WHITE_KING_POSITION = moves[(Position.white_dp["king"])]
    WHITE_QUEEN_POSITION = moves[(Position.white_dp["queen"])]

    WHITE_RIGHT_ROOK_POSITION = moves[(Position.white_dp["right_rook"])]
    WHITE_LEFT_ROOK_POSITION = moves[(Position.white_dp["left_rook"])]
    WHITE_RIGHT_KNIGHT_POSITION = moves[(Position.white_dp["right_knight"])]
    WHITE_LEFT_KNIGHT_POSITION = moves[(Position.white_dp["left_knight"])]
    WHITE_RIGHT_BISHOP_POSITION = moves[(Position.white_dp["right_bishop"])]
    WHITE_LEFT_BISHOP_POSITION = moves[(Position.white_dp["left_bishop"])]

    WHITE_PAWN_A7_POSITION = moves[(Position.white_dp["pawn1"])]
    WHITE_PAWN_B7_POSITION = moves[(Position.white_dp["pawn2"])]
    WHITE_PAWN_C7_POSITION = moves[(Position.white_dp["pawn3"])]
    WHITE_PAWN_D7_POSITION = moves[(Position.white_dp["pawn4"])]
    WHITE_PAWN_E7_POSITION = moves[(Position.white_dp["pawn5"])]
    WHITE_PAWN_F7_POSITION = moves[(Position.white_dp["pawn6"])]
    WHITE_PAWN_G7_POSITION = moves[(Position.white_dp["pawn7"])]
    WHITE_PAWN_H7_POSITION = moves[(Position.white_dp["pawn8"])]


    WHITE_PIECES_ALL_POSITIONS = [WHITE_KING_POSITION, WHITE_QUEEN_POSITION, WHITE_RIGHT_ROOK_POSITION, 
                                WHITE_LEFT_ROOK_POSITION, WHITE_RIGHT_KNIGHT_POSITION, 
                                WHITE_LEFT_KNIGHT_POSITION, WHITE_RIGHT_BISHOP_POSITION, 
                                WHITE_LEFT_BISHOP_POSITION, WHITE_PAWN_A7_POSITION,
                                WHITE_PAWN_B7_POSITION, WHITE_PAWN_C7_POSITION, WHITE_PAWN_D7_POSITION, 
                                WHITE_PAWN_E7_POSITION, WHITE_PAWN_F7_POSITION, WHITE_PAWN_G7_POSITION,
                                WHITE_PAWN_H7_POSITION]
        

class PieceCoordinates:
    """Contains the coordinates of each square in the game. The size of each square is 50 and that's 
    what the calculations here are based on."""

    zero_to_fifty = []
    count_for_zero_to_fifty = count(start=0, step=1)
    for _ in range(51):
        zero_to_fifty.append(next(count_for_zero_to_fifty))

    fifty_to_onehundred = []
    count_for_fifty_to_onehundred = count(start=50, step=1)
    for _ in range(50, 101):
        fifty_to_onehundred.append(next(count_for_fifty_to_onehundred))

    onehundred_to_onefifty = []
    count_for_onehundred_to_onefifty = count(start=100, step=1)
    for _ in range(100, 151):
        onehundred_to_onefifty.append(next(count_for_onehundred_to_onefifty))

    onefifty_to_twohundred = []
    count_for_onefifty_to_twohundred = count(start=150, step=1)
    for _ in range(150, 201):
        onefifty_to_twohundred.append(next(count_for_onefifty_to_twohundred))

    twohundred_to_twofifty = []
    count_for_twohundred_to_twofifty = count(start=200, step=1)
    for _ in range(200, 251):
        twohundred_to_twofifty.append(next(count_for_twohundred_to_twofifty))

    twofifty_to_threehundred = []
    count_for_twofifty_to_threehundred = count(start=250, step=1)
    for _ in range(250, 301):
        twofifty_to_threehundred.append(next(count_for_twofifty_to_threehundred))

    threehundred_to_threefifty = []
    count_for_threehundred_to_threefifty = count(start=300, step=1)
    for _ in range(300, 351):
        threehundred_to_threefifty.append(next(count_for_threehundred_to_threefifty))

    threefifty_to_fourhundred = []
    count_for_threefifty_to_fourhundred = count(start=350, step=1)
    for _ in range(350, 401):
        threefifty_to_fourhundred.append(next(count_for_threefifty_to_fourhundred))

    @classmethod
    def check_piece_coordinates(cls, x_coords, y_coords):
        """Takes in the X and Y coordinates of the mouseclick as an argument. These are provided by
        the event.pos in the game loop, which is in app.py. This function will check the entire chess 
        board, row by row, for which square was clicked."""
        def check_row_8():
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
        
        def check_row_7():
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
            else:
                return None
            
        def check_row_6():
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
        
        def check_row_5():
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
            
        def check_row_4():
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
        
        def check_row_3():
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
            
        def check_row_2():
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

        def check_row_1():
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

        returned_address = check_row_8()

        if returned_address == None:
            returned_address = check_row_7()

        if returned_address == None:
            returned_address = check_row_6()
            
        if returned_address == None:
            returned_address = check_row_5()

        if returned_address == None:
            returned_address = check_row_4()

        if returned_address == None:
            returned_address = check_row_3()

        if returned_address == None:
            returned_address = check_row_2()

        if returned_address == None:
            returned_address = check_row_1()

        if returned_address == None:
            logging.error(f"{CURRENT_TIME} - The program failed to check the selected piece's coordinates.")

        """Start from row 8. If the address is not found there, search in row 7. If not found there, then move to row 6. Continue
        down all the way to row 1. The address SHOULD be found by now."""

        return returned_address