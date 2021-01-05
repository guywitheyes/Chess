"""This file is used to run the game loop."""
import pygame
from game import Chessboard, Position
from config.piece_coordinates import ALL_PIECE_POSITIONS, PieceCoordinates, BlackCoordinates
from config import (SELECTED_SQUARE_COLOR, screen, user_selected_a_piece, piece_currently_selected,
        square_address, selected_piece)
from config.moves import moves
from sys import exit

def return_selected_piece():
    '''Checks the current position of every piece in the game and returns which piece was selected.'''
    selected_piece = None
    for piece in ALL_PIECE_POSITIONS: # check all pieces' current positions.
        if piece == square_address:
            # Then, 'piece' is the piece that the user has selected.
            selected_piece = piece
    return selected_piece


running = True
while running:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos # gets the coordinates of which square user clicked on.
                square_address = PieceCoordinates.check_piece_coordinates(x, y) # returns address on which those coordinates are. e.g: 'a3', 'b4', etc.
                
                selected_piece = return_selected_piece()
                print(selected_piece)
                
                if selected_piece != None:
                    user_selected_a_piece = True

    if user_selected_a_piece and square_address != None:
        if selected_piece != None:
            square_address_to_xy_coords = moves[square_address]

            Position.select_piece(square_address_to_xy_coords[0], square_address_to_xy_coords[1])
            piece_currently_selected = True
            pygame.display.update()

    if piece_currently_selected:
        Position.move_piece(BlackCoordinates.BLACK_KING_COORDINATES, 'd4')

    Chessboard() # Create chessboard.
                                    

