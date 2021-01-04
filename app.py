"""This file is used to run the game loop."""
import pygame
from game import Chessboard
from config import Position, PieceCoordinates
from sys import exit

running = True
while running:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # TODO: Figure out how to select a piece before moving it.

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                print(PieceCoordinates.check_piece_coordinates(x, y))
                # for piece_position in Position.BLACK_PIECES_ALL_POSITIONS:

                    # if PieceCoordinates.check_piece_coordinates(x, y):
                    #     Position.move_piece(Position.BLACK_KING_POSITION, 'd4')

    Chessboard() # Create chessboard.
