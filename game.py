"""This file is used to contain all the code, except the game loop and basic configuration that happens
in the config.py file."""

import pygame
import logging
from config import (CURRENT_TIME, CURRENT_DATE, SCREEN_HEIGHT, SCREEN_WIDTH, BLACK_SQUARE, WHITE_SQUARE,
        SQUARE_SIZE, screen, SELECTED_SQUARE_COLOR, piece_currently_selected)
from config.moves import SQUARE_SIZE, moves
from config.load_piece_images import PieceImages
from config.piece_coordinates import BlackCoordinates, WhiteCoordinates, BlackPosition, WhitePosition

logging.basicConfig(filename=f"logs/{str(CURRENT_DATE)}.log", filemode='a', level=logging.DEBUG)

pygame.display.init()


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
            Chessboard.BLACK_KING_BLIT = screen.blit(PieceImages.BLACK_KING, BlackCoordinates.BLACK_KING_COORDINATES)
            Chessboard.BLACK_QUEEN_BLIT = screen.blit(PieceImages.BLACK_QUEEN, BlackCoordinates.BLACK_QUEEN_COORDINATES)

            Chessboard.BLACK_ROOK_RIGHT_BLIT = screen.blit(PieceImages.BLACK_ROOK, BlackCoordinates.BLACK_RIGHT_ROOK_COORDINATES)
            Chessboard.BLACK_ROOK_LEFT_BLIT = screen.blit(PieceImages.BLACK_ROOK, BlackCoordinates.BLACK_LEFT_ROOK_COORDINATES)

            Chessboard.BLACK_KNIGHT_RIGHT_BLIT = screen.blit(PieceImages.BLACK_KNIGHT, BlackCoordinates.BLACK_RIGHT_KNIGHT_COORDINATES)
            Chessboard.BLACK_KNIGHT_LEFT_BLIT = screen.blit(PieceImages.BLACK_KNIGHT, BlackCoordinates.BLACK_LEFT_KNIGHT_COORDINATES)

            Chessboard.BLACK_BISHOP_RIGHT_BLIT = screen.blit(PieceImages.BLACK_BISHOP, BlackCoordinates.BLACK_RIGHT_BISHOP_COORDINATES)
            Chessboard.BLACK_BISHOP_LEFT_BLIT = screen.blit(PieceImages.BLACK_BISHOP, BlackCoordinates.BLACK_LEFT_BISHOP_COORDINATES)

            # TODO: To track each individual pawn, we'll have to create them one by one, without using for loops. It's gonna be repetitive code, but we've got no choice. Do it.
            # for i in Chessboard.moves[0]: # CREATING BLACK PAWNS
            #     if i in ('a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7'):
            #         screen.blit(PieceImages.BLACK_PAWN, Chessboard.moves[0][i])
            
            # CREATING BLACK PAWNS
            Chessboard.BLACK_PAWN_A7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackCoordinates.BLACK_PAWN_A7_COORDINATES)
            Chessboard.BLACK_PAWN_B7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackCoordinates.BLACK_PAWN_B7_COORDINATES)
            Chessboard.BLACK_PAWN_C7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackCoordinates.BLACK_PAWN_C7_COORDINATES)
            Chessboard.BLACK_PAWN_D7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackCoordinates.BLACK_PAWN_D7_COORDINATES)
            Chessboard.BLACK_PAWN_E7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackCoordinates.BLACK_PAWN_E7_COORDINATES)
            Chessboard.BLACK_PAWN_F7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackCoordinates.BLACK_PAWN_F7_COORDINATES)
            Chessboard.BLACK_PAWN_G7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackCoordinates.BLACK_PAWN_G7_COORDINATES)
            Chessboard.BLACK_PAWN_H7_BLIT = screen.blit(PieceImages.BLACK_PAWN, BlackCoordinates.BLACK_PAWN_H7_COORDINATES)

            # ----------------------------------------------------------------------------------------------

            # WHITE PIECES
            Chessboard.WHITE_KING_BLIT = screen.blit(PieceImages.WHITE_KING, WhiteCoordinates.WHITE_KING_COORDINATES)
            Chessboard.WHITE_QUEEN_BLIT = screen.blit(PieceImages.WHITE_QUEEN, WhiteCoordinates.WHITE_QUEEN_COORDINATES)

            Chessboard.WHITE_ROOK_BLIT1 = screen.blit(PieceImages.WHITE_ROOK, WhiteCoordinates.WHITE_RIGHT_ROOK_COORDINATES)
            Chessboard.WHITE_ROOK_BLIT2 = screen.blit(PieceImages.WHITE_ROOK, WhiteCoordinates.WHITE_LEFT_ROOK_COORDINATES)

            Chessboard.WHITE_KNIGHT_BLIT1 = screen.blit(PieceImages.WHITE_KNIGHT, WhiteCoordinates.WHITE_RIGHT_KNIGHT_COORDINATES)
            Chessboard.WHITE_KNIGHT_BLIT2 = screen.blit(PieceImages.WHITE_KNIGHT, WhiteCoordinates.WHITE_LEFT_KNIGHT_COORDINATES)

            Chessboard.WHITE_BISHOP_BLIT1 = screen.blit(PieceImages.WHITE_BISHOP, WhiteCoordinates.WHITE_RIGHT_BISHOP_COORDINATES)
            Chessboard.WHITE_BISHOP_BLIT2 = screen.blit(PieceImages.WHITE_BISHOP, WhiteCoordinates.WHITE_LEFT_BISHOP_COORDINATES)
            
            # CREATING WHITE PAWNS
            Chessboard.WHITE_PAWN_A7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhiteCoordinates.WHITE_PAWN_A7_COORDINATES)
            Chessboard.WHITE_PAWN_B7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhiteCoordinates.WHITE_PAWN_B7_COORDINATES)
            Chessboard.WHITE_PAWN_C7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhiteCoordinates.WHITE_PAWN_C7_COORDINATES)
            Chessboard.WHITE_PAWN_D7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhiteCoordinates.WHITE_PAWN_D7_COORDINATES)
            Chessboard.WHITE_PAWN_E7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhiteCoordinates.WHITE_PAWN_E7_COORDINATES)
            Chessboard.WHITE_PAWN_F7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhiteCoordinates.WHITE_PAWN_F7_COORDINATES)
            Chessboard.WHITE_PAWN_G7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhiteCoordinates.WHITE_PAWN_G7_COORDINATES)
            Chessboard.WHITE_PAWN_H7_BLIT = screen.blit(PieceImages.WHITE_PAWN, WhiteCoordinates.WHITE_PAWN_H7_COORDINATES)


        # FIXME: Since this function runs in the game loop, it keeps logging the same message over and over again. Fix this somehow.
        except Exception:
            logging.critical(f'{CURRENT_TIME} - An unexpected error occured while creating the chess pieces.')
    
    @classmethod
    def __init__(cls):
        cls.create_chessboard()
        cls.create_chess_pieces()

class Position:
    @classmethod
    def select_piece(cls, piece_x, piece_y):
        pygame.draw.rect(screen, SELECTED_SQUARE_COLOR, (piece_x, piece_y, 50, 50))

    @classmethod
    def move_piece(cls, piece, address):
            # FIXME: OK, 'piece' is the variable we're trying to change, but it's value is actually in 
            # coordinates like (200, 100). I think that's what is causing the issue here. I need some way 
            # to update the coordinates. When I do it manually, then it works. But when I try to use the 
            # piece parameter instead, it doesn't work. I don't know why.

            # Until you've built this function fully, here's how the pieces are actually moved: (in case you forget)
            BlackCoordinates.BLACK_KING_COORDINATES = moves["d4"]
            piece_currently_selected = False
            
            # print(piece)
            # print(address)
            # print(moves[address])