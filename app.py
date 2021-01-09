"""This file is used to run the game loop."""
import pygame
from game import Chessboard, Position
from config.piece_coordinates import (ALL_PIECE_POSITIONS, PieceCoordinates, BlackCoordinates, 
        WhiteCoordinates)
from config import (screen, user_selected_a_piece, piece_currently_selected,
        square_address, selected_piece, selected_piece_coordinates, SELECTED_SQUARE_COLOR)
from config.moves import moves
from sys import exit

def return_selected_piece_address():
    '''Checks the current position of every piece in the game and returns the address of which piece was selected.'''
    selected_piece = None
    for piece in ALL_PIECE_POSITIONS: # check all pieces' current positions.
        if piece == square_address:
            # Then, 'piece' is the piece that the user has selected.
            selected_piece = piece
    return selected_piece

def select_piece(event_coordinates):
    global user_selected_a_piece
    global selected_piece_coordinates
    global piece_currently_selected
    global square_address
    
    x, y = event_coordinates # Gets the coordinates(x, y) of which square user clicked on.
    selected_piece_coordinates = event_coordinates
    square_address = PieceCoordinates.check_piece_coordinates(x, y) # returns address on which those coordinates are. e.g: 'a3', 'b4', etc.

    selected_piece = return_selected_piece_address()
    print(selected_piece)

    
    if selected_piece != None: # did the user click on a square where there isn't a piece? then, let's not execute this.
        user_selected_a_piece = True


    if user_selected_a_piece and square_address != None:
        if selected_piece != None:
            x, y = moves[square_address]

            pygame.draw.rect(screen, SELECTED_SQUARE_COLOR, (x, y, 50, 50))
            pygame.display.update()

            piece_currently_selected = True

def move_piece(piece, address):
    global piece_currently_selected
    BlackCoordinates.update_coordinates(piece, address)
    WhiteCoordinates.update_coordinates(piece, address)
    piece_currently_selected = False # The piece has been moved, so we change this to False again.

running = True
while running:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                select_piece(event.pos)
                

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if piece_currently_selected and event.pos == selected_piece_coordinates:
                    move_piece(moves['d2'], 'd4') 
    
    Chessboard() # Create chessboard.
                                    

