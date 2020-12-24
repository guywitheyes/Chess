"""This file is used to contain all the code, except the game loop and basic configuration that happens
in the config.py file."""

import pygame
from config import *
import logging
from datetime import datetime

CURRENT_TIME = str(datetime.now().time().__str__()) # Used mostly in logging messages to log when the log message was made.
logging.basicConfig(filename=f"logs/{str(datetime.today().date().__str__())}.log", filemode='a', level=logging.DEBUG)

pygame.display.init()
screen_title = pygame.display.set_caption('Chess')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Chessboard:
    moves = ChessNotation.moves

    def create_chessboard():
        """Row is incremented after every loop so that we draw on the next row. The current_square
        is changed from BLACK_SQUARE to WHITE_SQUARE and from WHITE_SQUARE to BLACK_SQUARE again and
        again, because otherwise it would simply create a straight line of black and white squares.
        In chess, the black and white squares are diaognal. Hence the constant switching from one to 
        the other."""
        
        row = 0
        current_square = BLACK_SQUARE
        try:
            for i in range(0, 8):
                for j in range(0, 8):
                    if current_square == BLACK_SQUARE:
                        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*j, SQUARE_SIZE*row))
                        current_square = WHITE_SQUARE

                    elif current_square == WHITE_SQUARE:
                        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*j, SQUARE_SIZE*row))
                        current_square = BLACK_SQUARE
                row += 1
                if i % 2 == 1:
                    current_square = BLACK_SQUARE 
                elif i % 2 == 0:
                    current_square = WHITE_SQUARE
        except Exception:
            logging.critical(f'{CURRENT_TIME} - An unexpected error occured while creating the chessboard. The chessboard could not be created.')
            
    def create_chess_pieces():
        # BLACK PIECES
        screen.blit(BlackPieces.BLACK_KING, Chessboard.moves[0]['e8'])
        screen.blit(BlackPieces.BLACK_QUEEN, Chessboard.moves[0]['d8'])

        screen.blit(BlackPieces.BLACK_ROOK, Chessboard.moves[0]['a8'])
        screen.blit(BlackPieces.BLACK_ROOK, Chessboard.moves[0]['h8'])

        screen.blit(BlackPieces.BLACK_KNIGHT, Chessboard.moves[0]['b8'])
        screen.blit(BlackPieces.BLACK_KNIGHT, Chessboard.moves[0]['g8'])

        screen.blit(BlackPieces.BLACK_BISHOP, Chessboard.moves[0]['c8'])
        screen.blit(BlackPieces.BLACK_BISHOP, Chessboard.moves[0]['f8'])

        for i in Chessboard.moves[1]: # CREATING BLACK PAWNS
            screen.blit(BlackPieces.BLACK_PAWN, Chessboard.moves[1][i])

        # WHITE PIECES
        screen.blit(WhitePieces.WHITE_KING, Chessboard.moves[7]['e1'])
        screen.blit(WhitePieces.WHITE_QUEEN, Chessboard.moves[7]['d1'])

        screen.blit(WhitePieces.WHITE_ROOK, Chessboard.moves[7]['a1'])
        screen.blit(WhitePieces.WHITE_ROOK, Chessboard.moves[7]['h1'])

        screen.blit(WhitePieces.WHITE_KNIGHT, Chessboard.moves[7]['b1'])
        screen.blit(WhitePieces.WHITE_KNIGHT, Chessboard.moves[7]['g1'])

        screen.blit(WhitePieces.WHITE_BISHOP, Chessboard.moves[7]['c1'])
        screen.blit(WhitePieces.WHITE_BISHOP, Chessboard.moves[7]['f1'])
        
        for i in Chessboard.moves[6]: # CREATING WHITE PAWNS
            screen.blit(WhitePieces.WHITE_PAWN, Chessboard.moves[6][i])

    def __init__(self):
        Chessboard.create_chessboard()
        Chessboard.create_chess_pieces()

class Pieces:
    moves = ChessNotation.moves