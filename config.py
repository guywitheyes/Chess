import pygame


BLACK_SQUARE = pygame.image.load('assets/black-square.png')
WHITE_SQUARE = pygame.image.load('assets/white-square.png')
SQUARE_SIZE = 50

(SCREEN_WIDTH, SCREEN_HEIGHT) = (400, 400)

class BlackPieces:
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
    
class WhitePieces:
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
     moves = [ # Sets up the chess notation.
        { #Row: 0
            'a8': (SQUARE_SIZE*0, SQUARE_SIZE*0),
            'b8': (SQUARE_SIZE*1, SQUARE_SIZE*0),
            'c8': (SQUARE_SIZE*2, SQUARE_SIZE*0),
            'd8': (SQUARE_SIZE*3, SQUARE_SIZE*0),
            'e8': (SQUARE_SIZE*4, SQUARE_SIZE*0),
            'f8': (SQUARE_SIZE*5, SQUARE_SIZE*0),
            'g8': (SQUARE_SIZE*6, SQUARE_SIZE*0),
            'h8': (SQUARE_SIZE*7, SQUARE_SIZE*0)
        },
        { #Row: 1
            'a7': (SQUARE_SIZE*0, SQUARE_SIZE*1),
            'b7': (SQUARE_SIZE*1, SQUARE_SIZE*1),
            'c7': (SQUARE_SIZE*2, SQUARE_SIZE*1),
            'd7': (SQUARE_SIZE*3, SQUARE_SIZE*1),
            'e7': (SQUARE_SIZE*4, SQUARE_SIZE*1),
            'f7': (SQUARE_SIZE*5, SQUARE_SIZE*1),
            'g7': (SQUARE_SIZE*6, SQUARE_SIZE*1),
            'h7': (SQUARE_SIZE*7, SQUARE_SIZE*1)
        },
        { #Row: 2
            'a6': (SQUARE_SIZE*0, SQUARE_SIZE*2),
            'b6': (SQUARE_SIZE*1, SQUARE_SIZE*2),
            'c6': (SQUARE_SIZE*2, SQUARE_SIZE*2),
            'd6': (SQUARE_SIZE*3, SQUARE_SIZE*2),
            'e6': (SQUARE_SIZE*4, SQUARE_SIZE*2),
            'f6': (SQUARE_SIZE*5, SQUARE_SIZE*2),
            'g6': (SQUARE_SIZE*6, SQUARE_SIZE*2),
            'h6': (SQUARE_SIZE*7, SQUARE_SIZE*2)
        },
        { #Row: 3
            'a5': (SQUARE_SIZE*0, SQUARE_SIZE*3),
            'b5': (SQUARE_SIZE*1, SQUARE_SIZE*3),
            'c5': (SQUARE_SIZE*2, SQUARE_SIZE*3),
            'd5': (SQUARE_SIZE*3, SQUARE_SIZE*3),
            'e5': (SQUARE_SIZE*4, SQUARE_SIZE*3),
            'f5': (SQUARE_SIZE*5, SQUARE_SIZE*3),
            'g5': (SQUARE_SIZE*6, SQUARE_SIZE*3),
            'h5': (SQUARE_SIZE*7, SQUARE_SIZE*3)
        },
        { #Row: 4
            'a4': (SQUARE_SIZE*0, SQUARE_SIZE*4),
            'b4': (SQUARE_SIZE*1, SQUARE_SIZE*4),
            'c4': (SQUARE_SIZE*2, SQUARE_SIZE*4),
            'd4': (SQUARE_SIZE*3, SQUARE_SIZE*4),
            'e4': (SQUARE_SIZE*4, SQUARE_SIZE*4),
            'f4': (SQUARE_SIZE*5, SQUARE_SIZE*4),
            'g4': (SQUARE_SIZE*6, SQUARE_SIZE*4),
            'h4': (SQUARE_SIZE*7, SQUARE_SIZE*4)
        },
        { #Row: 5
            'a3': (SQUARE_SIZE*0, SQUARE_SIZE*5),
            'b3': (SQUARE_SIZE*1, SQUARE_SIZE*5),
            'c3': (SQUARE_SIZE*2, SQUARE_SIZE*5),
            'd3': (SQUARE_SIZE*3, SQUARE_SIZE*5),
            'e3': (SQUARE_SIZE*4, SQUARE_SIZE*5),
            'f3': (SQUARE_SIZE*5, SQUARE_SIZE*5),
            'g3': (SQUARE_SIZE*6, SQUARE_SIZE*5),
            'h3': (SQUARE_SIZE*7, SQUARE_SIZE*5)
        },
        { #Row: 6
            'a2': (SQUARE_SIZE*0, SQUARE_SIZE*6),
            'b2': (SQUARE_SIZE*1, SQUARE_SIZE*6),
            'c2': (SQUARE_SIZE*2, SQUARE_SIZE*6),
            'd2': (SQUARE_SIZE*3, SQUARE_SIZE*6),
            'e2': (SQUARE_SIZE*4, SQUARE_SIZE*6),
            'f2': (SQUARE_SIZE*5, SQUARE_SIZE*6),
            'g2': (SQUARE_SIZE*6, SQUARE_SIZE*6),
            'h2': (SQUARE_SIZE*7, SQUARE_SIZE*6)
        },
        { #Row: 7
            'a1': (SQUARE_SIZE*0, SQUARE_SIZE*7),
            'b1': (SQUARE_SIZE*1, SQUARE_SIZE*7),
            'c1': (SQUARE_SIZE*2, SQUARE_SIZE*7),
            'd1': (SQUARE_SIZE*3, SQUARE_SIZE*7),
            'e1': (SQUARE_SIZE*4, SQUARE_SIZE*7),
            'f1': (SQUARE_SIZE*5, SQUARE_SIZE*7),
            'g1': (SQUARE_SIZE*6, SQUARE_SIZE*7),
            'h1': (SQUARE_SIZE*7, SQUARE_SIZE*7)
        }
    ]