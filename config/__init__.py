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
