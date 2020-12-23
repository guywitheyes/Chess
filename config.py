import pygame


BLACK_SQUARE = pygame.image.load('assets/black-square.png')
WHITE_SQUARE = pygame.image.load('assets/white-square.png')
SQUARE_SIZE = 50

(SCREEN_WIDTH, SCREEN_HEIGHT) = (440, 480)

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