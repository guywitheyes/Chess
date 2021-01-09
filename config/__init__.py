import pygame
from itertools import count
from datetime import datetime
from config.load_piece_images import PieceImages
from config.moves import moves
import logging


BLACK_SQUARE = pygame.image.load('assets/black-square.png')
WHITE_SQUARE = pygame.image.load('assets/white-square.png')
SQUARE_SIZE = 50

(SCREEN_WIDTH, SCREEN_HEIGHT) = (400, 400)

CURRENT_DATE = str(datetime.today().date().__str__()) # Used mostly in logging messages.
CURRENT_TIME = str(datetime.now().time().__str__()) # Used mostly in logging messages.

SELECTED_SQUARE_COLOR = (10, 255, 40) # RGB Colors (Red, Green, Blue)

screen_title = pygame.display.set_caption('Chess')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

selected_piece = None
square_address = None

selected_piece_coordinates = None

'''Difference between these two is that when user_selects_a_piece, we run the select() function on it.
Then, by selecting it, piece_currently_selected becomes True. Since a piece is now selected, the 
move_piece() function will now be run to move the piece and change piece_currently_selected back to False.'''

user_selected_a_piece = False # Did the user click on a piece and select it?
piece_currently_selected = False # Is a piece currently selected?