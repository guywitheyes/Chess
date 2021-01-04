"""This file is used to contain all the code, except the game loop and basic configuration that happens
in the config.py file."""

import pygame
from config import (SCREEN_WIDTH, SCREEN_HEIGHT, BLACK_SQUARE, WHITE_SQUARE, 
                    SQUARE_SIZE, PieceImages, BlackPosition, WhitePosition, ChessNotation, 
                    CURRENT_DATE, CURRENT_TIME)
import logging
from database.moves import moves

logging.basicConfig(filename=f"logs/{str(CURRENT_DATE)}.log", filemode='a', level=logging.DEBUG)

pygame.display.init()
screen_title = pygame.display.set_caption('Chess')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Chessboard:
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
        try:
            Chessboard.BLACK_KING_BLIT = screen.blit(PieceImages.BLACK_KING, BlackPosition.BLACK_KING_POSITION)
            Chessboard.BLACK_QUEEN_BLIT = screen.blit(PieceImages.BLACK_QUEEN, BlackPosition.BLACK_QUEEN_POSITION)

            Chessboard.BLACK_ROOK_RIGHT_BLIT = screen.blit(PieceImages.BLACK_ROOK, BlackPosition.BLACK_RIGHT_ROOK_POSITION)
            Chessboard.BLACK_ROOK_LEFT_BLIT = screen.blit(PieceImages.BLACK_ROOK, BlackPosition.BLACK_LEFT_ROOK_POSITION)

            Chessboard.BLACK_KNIGHT_RIGHT_BLIT = screen.blit(PieceImages.BLACK_KNIGHT, BlackPosition.BLACK_RIGHT_KNIGHT_POSITION)
            Chessboard.BLACK_KNIGHT_LEFT_BLIT = screen.blit(PieceImages.BLACK_KNIGHT, BlackPosition.BLACK_LEFT_KNIGHT_POSITION)

            Chessboard.BLACK_BISHOP_RIGHT_BLIT = screen.blit(PieceImages.BLACK_BISHOP, BlackPosition.BLACK_RIGHT_BISHOP_POSITION)
            Chessboard.BLACK_BISHOP_LEFT_BLIT = screen.blit(PieceImages.BLACK_BISHOP, BlackPosition.BLACK_LEFT_BISHOP_POSITION)

            # TODO: To track each individual pawn, we'll have to create them one by one, without using for loops. It's gonna be repetitive code, but we've got no choice. Do it.
            # for i in Chessboard.moves[0]: # CREATING BLACK PAWNS
            #     if i in ('a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'):
            #         screen.blit(PieceImages.BLACK_PAWN, Chessboard.moves[0][i])
            
            # CREATING BLACK PAWNS
            Chessboard.BLACK_PAWN_A7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackPosition.BLACK_PAWN_A7_POSITION)
            Chessboard.BLACK_PAWN_B7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackPosition.BLACK_PAWN_B7_POSITION)
            Chessboard.BLACK_PAWN_C7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackPosition.BLACK_PAWN_C7_POSITION)
            Chessboard.BLACK_PAWN_D7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackPosition.BLACK_PAWN_D7_POSITION)
            Chessboard.BLACK_PAWN_E7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackPosition.BLACK_PAWN_E7_POSITION)
            Chessboard.BLACK_PAWN_F7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackPosition.BLACK_PAWN_F7_POSITION)
            Chessboard.BLACK_PAWN_G7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackPosition.BLACK_PAWN_G7_POSITION)
            Chessboard.BLACK_PAWN_H7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackPosition.BLACK_PAWN_H7_POSITION)

            # ----------------------------------------------------------------------------------------------

            # WHITE PIECES
            Chessboard.WHITE_KING_BLIT = screen.blit(PieceImages.WHITE_KING, WhitePosition.WHITE_KING_POSITION)
            Chessboard.WHITE_QUEEN_BLIT = screen.blit(PieceImages.WHITE_QUEEN, WhitePosition.WHITE_QUEEN_POSITION)

            Chessboard.WHITE_ROOK_BLIT1 = screen.blit(PieceImages.WHITE_ROOK, WhitePosition.WHITE_RIGHT_ROOK_POSITION)
            Chessboard.WHITE_ROOK_BLIT2 = screen.blit(PieceImages.WHITE_ROOK, WhitePosition.WHITE_LEFT_ROOK_POSITION)

            Chessboard.WHITE_KNIGHT_BLIT1 = screen.blit(PieceImages.WHITE_KNIGHT, WhitePosition.WHITE_RIGHT_KNIGHT_POSITION)
            Chessboard.WHITE_KNIGHT_BLIT2 = screen.blit(PieceImages.WHITE_KNIGHT, WhitePosition.WHITE_LEFT_KNIGHT_POSITION)

            Chessboard.WHITE_BISHOP_BLIT1 = screen.blit(PieceImages.WHITE_BISHOP, WhitePosition.WHITE_RIGHT_BISHOP_POSITION)
            Chessboard.WHITE_BISHOP_BLIT2 = screen.blit(PieceImages.WHITE_BISHOP, WhitePosition.WHITE_LEFT_BISHOP_POSITION)
            
            # CREATING WHITE PAWNS
            Chessboard.WHITE_PAWN_A7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhitePosition.WHITE_PAWN_A7_POSITION)
            Chessboard.WHITE_PAWN_B7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhitePosition.WHITE_PAWN_B7_POSITION)
            Chessboard.WHITE_PAWN_C7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhitePosition.WHITE_PAWN_C7_POSITION)
            Chessboard.WHITE_PAWN_D7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhitePosition.WHITE_PAWN_D7_POSITION)
            Chessboard.WHITE_PAWN_E7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhitePosition.WHITE_PAWN_E7_POSITION)
            Chessboard.WHITE_PAWN_F7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhitePosition.WHITE_PAWN_F7_POSITION)
            Chessboard.WHITE_PAWN_G7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhitePosition.WHITE_PAWN_G7_POSITION)
            Chessboard.WHITE_PAWN_H7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhitePosition.WHITE_PAWN_H7_POSITION)


        # FIXME: Since this function runs in the game loop, it keeps logging the same message over and over again. Fix this somehow.
        except Exception:
            logging.critical(f'{CURRENT_TIME} - An unexpected error occured while creating the chess pieces.')
    
    @classmethod
    def __init__(cls):
        cls.create_chessboard()
        cls.create_chess_pieces()
