"""This file is used to contain all the code, except the game loop and basic configuration that happens
in the config.py file."""

import pygame
from config import ChessPieces
from config import SCREEN_HEIGHT, SCREEN_WIDTH, SQUARE_SIZE, BLACK_SQUARE, WHITE_SQUARE


pygame.display.init()
screen_title = pygame.display.set_caption('Chess')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Chessboard:
    # TODO: We should be able to convert each of these into for loops. Remove all the duplicate code.
    # TODO: We must also somehow assign the Chess Address variables here. (a1, b3, d8, etc.)
    moves = [ # Sets up the chess notation.
        {
            'a8': (SQUARE_SIZE*0, SQUARE_SIZE*1),
            'b8': (SQUARE_SIZE*1, SQUARE_SIZE*1),
            'c8': (SQUARE_SIZE*2, SQUARE_SIZE*1),
            'd8': (SQUARE_SIZE*3, SQUARE_SIZE*1),
            'e8': (SQUARE_SIZE*4, SQUARE_SIZE*1),
            'f8': (SQUARE_SIZE*5, SQUARE_SIZE*1),
            'g8': (SQUARE_SIZE*6, SQUARE_SIZE*1),
            'h8': (SQUARE_SIZE*7, SQUARE_SIZE*1)
        },
        {
            'a7': (SQUARE_SIZE*0, SQUARE_SIZE*2),
            'b7': (SQUARE_SIZE*1, SQUARE_SIZE*2),
            'c7': (SQUARE_SIZE*2, SQUARE_SIZE*2),
            'd7': (SQUARE_SIZE*3, SQUARE_SIZE*2),
            'e7': (SQUARE_SIZE*4, SQUARE_SIZE*2),
            'f7': (SQUARE_SIZE*5, SQUARE_SIZE*2),
            'g7': (SQUARE_SIZE*6, SQUARE_SIZE*2),
            'h7': (SQUARE_SIZE*7, SQUARE_SIZE*2)
        },
        {
            'a6': (SQUARE_SIZE*0, SQUARE_SIZE*3),
            'b6': (SQUARE_SIZE*1, SQUARE_SIZE*3),
            'c6': (SQUARE_SIZE*2, SQUARE_SIZE*3),
            'd6': (SQUARE_SIZE*3, SQUARE_SIZE*3),
            'e6': (SQUARE_SIZE*4, SQUARE_SIZE*3),
            'f6': (SQUARE_SIZE*5, SQUARE_SIZE*3),
            'g6': (SQUARE_SIZE*6, SQUARE_SIZE*3),
            'h6': (SQUARE_SIZE*7, SQUARE_SIZE*3)
        },
        {
            'a5': (SQUARE_SIZE*0, SQUARE_SIZE*4),
            'b5': (SQUARE_SIZE*1, SQUARE_SIZE*4),
            'c5': (SQUARE_SIZE*2, SQUARE_SIZE*4),
            'd5': (SQUARE_SIZE*3, SQUARE_SIZE*4),
            'e5': (SQUARE_SIZE*4, SQUARE_SIZE*4),
            'f5': (SQUARE_SIZE*5, SQUARE_SIZE*4),
            'g5': (SQUARE_SIZE*6, SQUARE_SIZE*4),
            'h5': (SQUARE_SIZE*7, SQUARE_SIZE*4)
        },
        {
            'a4': (SQUARE_SIZE*0, SQUARE_SIZE*5),
            'b4': (SQUARE_SIZE*1, SQUARE_SIZE*5),
            'c4': (SQUARE_SIZE*2, SQUARE_SIZE*5),
            'd4': (SQUARE_SIZE*3, SQUARE_SIZE*5),
            'e4': (SQUARE_SIZE*4, SQUARE_SIZE*5),
            'f4': (SQUARE_SIZE*5, SQUARE_SIZE*5),
            'g4': (SQUARE_SIZE*6, SQUARE_SIZE*5),
            'h4': (SQUARE_SIZE*7, SQUARE_SIZE*5)
        },
        {
            'a3': (SQUARE_SIZE*0, SQUARE_SIZE*6),
            'b3': (SQUARE_SIZE*1, SQUARE_SIZE*6),
            'c3': (SQUARE_SIZE*2, SQUARE_SIZE*6),
            'd3': (SQUARE_SIZE*3, SQUARE_SIZE*6),
            'e3': (SQUARE_SIZE*4, SQUARE_SIZE*6),
            'f3': (SQUARE_SIZE*5, SQUARE_SIZE*6),
            'g3': (SQUARE_SIZE*6, SQUARE_SIZE*6),
            'h3': (SQUARE_SIZE*7, SQUARE_SIZE*6)
        },
        {
            'a2': (SQUARE_SIZE*0, SQUARE_SIZE*7),
            'b2': (SQUARE_SIZE*1, SQUARE_SIZE*7),
            'c2': (SQUARE_SIZE*2, SQUARE_SIZE*7),
            'd2': (SQUARE_SIZE*3, SQUARE_SIZE*7),
            'e2': (SQUARE_SIZE*4, SQUARE_SIZE*7),
            'f2': (SQUARE_SIZE*5, SQUARE_SIZE*7),
            'g2': (SQUARE_SIZE*6, SQUARE_SIZE*7),
            'h2': (SQUARE_SIZE*7, SQUARE_SIZE*7)
        },
        {
            'a1': (SQUARE_SIZE*0, SQUARE_SIZE*8),
            'b1': (SQUARE_SIZE*1, SQUARE_SIZE*8),
            'c1': (SQUARE_SIZE*2, SQUARE_SIZE*8),
            'd1': (SQUARE_SIZE*3, SQUARE_SIZE*8),
            'e1': (SQUARE_SIZE*4, SQUARE_SIZE*8),
            'f1': (SQUARE_SIZE*5, SQUARE_SIZE*8),
            'g1': (SQUARE_SIZE*6, SQUARE_SIZE*8),
            'h1': (SQUARE_SIZE*7, SQUARE_SIZE*8)
        }
    ]

    def create_chessboard():
        row = 1
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

        row = 2
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

        row = 3
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

        row = 4
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

        row = 5
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

        row = 6
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

        row = 7
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

        row = 8
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))
    
    def create_chess_pieces():
        screen.blit(ChessPieces.BLACK_BISHOP, Chessboard.moves[1]['a7'])

    def __init__(self):
        Chessboard.create_chessboard()
        Chessboard.create_chess_pieces()