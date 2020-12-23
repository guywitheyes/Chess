import pygame
from chessboard import Chessboard, screen
from sys import exit

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('brown')
    Chessboard() # Create chessboard.