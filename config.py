import pygame
from itertools import count
from datetime import datetime
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
    default_positions =  [
    { 'Black':
        {
            'king': 'e8',
            'queen': 'd8',
            'right_rook': 'h8',
            'left_rook': 'a8',
            'right_knight': 'g8',
            'left_knight': 'b8',
            'right_bishop': 'f8',
            'left_bishop': 'c8',

            # from left to right on the chessboard:
            'pawn1': 'a7',
            'pawn2': 'b7',
            'pawn3': 'c7',
            'pawn4': 'd7',
            'pawn5': 'e7',
            'pawn6': 'f7',
            'pawn7': 'g7',
            'pawn8': 'h7',
        }
    }, 
    { 'White': 
        {
            'king': 'e1',
            'queen': 'd1',
            'right_rook': 'h1',
            'left_rook': 'a1',
            'right_knight': 'g1',
            'left_knight': 'b1',
            'right_bishop': 'f1',
            'left_bishop': 'c1',

            # from left to right on the chessboard:
            'pawn1': 'a2',
            'pawn2': 'b2',
            'pawn3': 'c2',
            'pawn4': 'd2',
            'pawn5': 'e2',
            'pawn6': 'f2',
            'pawn7': 'g2',
            'pawn8': 'h2',
        }
    }
    ]
    
    # TODO: Move this moves dictionary to a JSON database.
    # TODO: Remove the square brackets and turn moves into a dictionary, not a list. You can then remove the [0] from everywhere.
    # Addresses of all squares on the Chessboard.
    moves = {    #Row: 1
        'a8': (SQUARE_SIZE*0, SQUARE_SIZE*0),
        'b8': (SQUARE_SIZE*1, SQUARE_SIZE*0),
        'c8': (SQUARE_SIZE*2, SQUARE_SIZE*0),
        'd8': (SQUARE_SIZE*3, SQUARE_SIZE*0),
        'e8': (SQUARE_SIZE*4, SQUARE_SIZE*0),
        'f8': (SQUARE_SIZE*5, SQUARE_SIZE*0),
        'g8': (SQUARE_SIZE*6, SQUARE_SIZE*0),
        'h8': (SQUARE_SIZE*7, SQUARE_SIZE*0),

        #Row: 2
        'a7': (SQUARE_SIZE*0, SQUARE_SIZE*1),
        'b7': (SQUARE_SIZE*1, SQUARE_SIZE*1),
        'c7': (SQUARE_SIZE*2, SQUARE_SIZE*1),
        'd7': (SQUARE_SIZE*3, SQUARE_SIZE*1),
        'e7': (SQUARE_SIZE*4, SQUARE_SIZE*1),
        'f7': (SQUARE_SIZE*5, SQUARE_SIZE*1),
        'g7': (SQUARE_SIZE*6, SQUARE_SIZE*1),
        'h7': (SQUARE_SIZE*7, SQUARE_SIZE*1),

        #Row: 3
        'a6': (SQUARE_SIZE*0, SQUARE_SIZE*2),
        'b6': (SQUARE_SIZE*1, SQUARE_SIZE*2),
        'c6': (SQUARE_SIZE*2, SQUARE_SIZE*2),
        'd6': (SQUARE_SIZE*3, SQUARE_SIZE*2),
        'e6': (SQUARE_SIZE*4, SQUARE_SIZE*2),
        'f6': (SQUARE_SIZE*5, SQUARE_SIZE*2),
        'g6': (SQUARE_SIZE*6, SQUARE_SIZE*2),
        'h6': (SQUARE_SIZE*7, SQUARE_SIZE*2),

        #Row: 4
        'a5': (SQUARE_SIZE*0, SQUARE_SIZE*3),
        'b5': (SQUARE_SIZE*1, SQUARE_SIZE*3),
        'c5': (SQUARE_SIZE*2, SQUARE_SIZE*3),
        'd5': (SQUARE_SIZE*3, SQUARE_SIZE*3),
        'e5': (SQUARE_SIZE*4, SQUARE_SIZE*3),
        'f5': (SQUARE_SIZE*5, SQUARE_SIZE*3),
        'g5': (SQUARE_SIZE*6, SQUARE_SIZE*3),
        'h5': (SQUARE_SIZE*7, SQUARE_SIZE*3),

        #Row: 5
        'a4': (SQUARE_SIZE*0, SQUARE_SIZE*4),
        'b4': (SQUARE_SIZE*1, SQUARE_SIZE*4),
        'c4': (SQUARE_SIZE*2, SQUARE_SIZE*4),
        'd4': (SQUARE_SIZE*3, SQUARE_SIZE*4),
        'e4': (SQUARE_SIZE*4, SQUARE_SIZE*4),
        'f4': (SQUARE_SIZE*5, SQUARE_SIZE*4),
        'g4': (SQUARE_SIZE*6, SQUARE_SIZE*4),
        'h4': (SQUARE_SIZE*7, SQUARE_SIZE*4),

        #Row: 6
        'a3': (SQUARE_SIZE*0, SQUARE_SIZE*5),
        'b3': (SQUARE_SIZE*1, SQUARE_SIZE*5),
        'c3': (SQUARE_SIZE*2, SQUARE_SIZE*5),
        'd3': (SQUARE_SIZE*3, SQUARE_SIZE*5),
        'e3': (SQUARE_SIZE*4, SQUARE_SIZE*5),
        'f3': (SQUARE_SIZE*5, SQUARE_SIZE*5),
        'g3': (SQUARE_SIZE*6, SQUARE_SIZE*5),
        'h3': (SQUARE_SIZE*7, SQUARE_SIZE*5),

        #Row: 7
        'a2': (SQUARE_SIZE*0, SQUARE_SIZE*6),
        'b2': (SQUARE_SIZE*1, SQUARE_SIZE*6),
        'c2': (SQUARE_SIZE*2, SQUARE_SIZE*6),
        'd2': (SQUARE_SIZE*3, SQUARE_SIZE*6),
        'e2': (SQUARE_SIZE*4, SQUARE_SIZE*6),
        'f2': (SQUARE_SIZE*5, SQUARE_SIZE*6),
        'g2': (SQUARE_SIZE*6, SQUARE_SIZE*6),
        'h2': (SQUARE_SIZE*7, SQUARE_SIZE*6),

        #Row: 8
        'a1': (SQUARE_SIZE*0, SQUARE_SIZE*7),
        'b1': (SQUARE_SIZE*1, SQUARE_SIZE*7),
        'c1': (SQUARE_SIZE*2, SQUARE_SIZE*7),
        'd1': (SQUARE_SIZE*3, SQUARE_SIZE*7),
        'e1': (SQUARE_SIZE*4, SQUARE_SIZE*7),
        'f1': (SQUARE_SIZE*5, SQUARE_SIZE*7),
        'g1': (SQUARE_SIZE*6, SQUARE_SIZE*7),
        'h1': (SQUARE_SIZE*7, SQUARE_SIZE*7),
    }

class Position:

    class BlackPosition:
        BLACK_KING_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["king"])]
        BLACK_QUEEN_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["queen"])]

        BLACK_RIGHT_ROOK_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["right_rook"])]
        BLACK_LEFT_ROOK_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["left_rook"])]
        BLACK_RIGHT_KNIGHT_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["right_knight"])]
        BLACK_LEFT_KNIGHT_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["left_knight"])]
        BLACK_RIGHT_BISHOP_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["right_bishop"])]
        BLACK_LEFT_BISHOP_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["left_bishop"])]

        BLACK_PAWN_A7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["pawn1"])]
        BLACK_PAWN_B7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["pawn2"])]
        BLACK_PAWN_C7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["pawn3"])]
        BLACK_PAWN_D7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["pawn4"])]
        BLACK_PAWN_E7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["pawn5"])]
        BLACK_PAWN_F7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["pawn6"])]
        BLACK_PAWN_G7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["pawn7"])]
        BLACK_PAWN_H7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[0]["Black"]["pawn8"])]


        BLACK_PIECES_ALL_POSITIONS = [BLACK_KING_POSITION, BLACK_QUEEN_POSITION, BLACK_RIGHT_ROOK_POSITION, 
                                    BLACK_LEFT_ROOK_POSITION, BLACK_RIGHT_KNIGHT_POSITION, 
                                    BLACK_LEFT_KNIGHT_POSITION, BLACK_RIGHT_BISHOP_POSITION, 
                                    BLACK_LEFT_BISHOP_POSITION, BLACK_PAWN_A7_POSITION,
                                    BLACK_PAWN_B7_POSITION, BLACK_PAWN_C7_POSITION, BLACK_PAWN_D7_POSITION, 
                                    BLACK_PAWN_E7_POSITION, BLACK_PAWN_F7_POSITION, BLACK_PAWN_G7_POSITION,
                                    BLACK_PAWN_H7_POSITION]
    
    # TODO: Add the POSITIONs for all the white pieces, including white pawns.
    class WhitePosition:
        WHITE_KING_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["king"])]
        WHITE_QUEEN_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["queen"])]

        WHITE_RIGHT_ROOK_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["right_rook"])]
        WHITE_LEFT_ROOK_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["left_rook"])]
        WHITE_RIGHT_KNIGHT_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["right_knight"])]
        WHITE_LEFT_KNIGHT_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["left_knight"])]
        WHITE_RIGHT_BISHOP_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["right_bishop"])]
        WHITE_LEFT_BISHOP_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["left_bishop"])]

        WHITE_PAWN_A7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["pawn1"])]
        WHITE_PAWN_B7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["pawn2"])]
        WHITE_PAWN_C7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["pawn3"])]
        WHITE_PAWN_D7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["pawn4"])]
        WHITE_PAWN_E7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["pawn5"])]
        WHITE_PAWN_F7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["pawn6"])]
        WHITE_PAWN_G7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["pawn7"])]
        WHITE_PAWN_H7_POSITION = ChessNotation.moves[(ChessNotation.default_positions[1]["White"]["pawn8"])]


        WHITE_PIECES_ALL_POSITIONS = [WHITE_KING_POSITION, WHITE_QUEEN_POSITION, WHITE_RIGHT_ROOK_POSITION, 
                                    WHITE_LEFT_ROOK_POSITION, WHITE_RIGHT_KNIGHT_POSITION, 
                                    WHITE_LEFT_KNIGHT_POSITION, WHITE_RIGHT_BISHOP_POSITION, 
                                    WHITE_LEFT_BISHOP_POSITION, WHITE_PAWN_A7_POSITION,
                                    WHITE_PAWN_B7_POSITION, WHITE_PAWN_C7_POSITION, WHITE_PAWN_D7_POSITION, 
                                    WHITE_PAWN_E7_POSITION, WHITE_PAWN_F7_POSITION, WHITE_PAWN_G7_POSITION,
                                    WHITE_PAWN_H7_POSITION]
        

    # TODO: Put all the white pieces' positions in a list, just like we did with the Black pieces' positions above.

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
            piece = ChessNotation.moves[position]

    

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