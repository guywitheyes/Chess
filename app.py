import pygame
from sys import exit

(SCREEN_WIDTH, SCREEN_HEIGHT) = (440, 480)
BLACK_SQUARE = pygame.image.load('assets/black-square.png')
WHITE_SQUARE = pygame.image.load('assets/white-square.png')
SQUARE_SIZE = 50

pygame.display.init()
screen_title = pygame.display.set_caption('Chess')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Chessboard:
    # TODO: We should be able to convert each of these into for loops. Remove all the duplicate code.
    # TODO: We must also somehow assign the Chess Address variables here. (a1, b3, d8, etc.)
    
    def create_row1(row=1):
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

    def create_row2(row=2):
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

    def create_row3(row=3):
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

    def create_row4(row=4):
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

    def create_row5(row=5):
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

    def create_row6(row=6):
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

    def create_row7(row=7):
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

    def create_row8(row=8):
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*0, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*1, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*2, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*3, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*4, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*5, SQUARE_SIZE*row))
        screen.blit(WHITE_SQUARE, (SQUARE_SIZE*6, SQUARE_SIZE*row))
        screen.blit(BLACK_SQUARE, (SQUARE_SIZE*7, SQUARE_SIZE*row))

    @staticmethod
    def create_chessboard():
        Chessboard.create_row1()
        Chessboard.create_row2()
        Chessboard.create_row3()
        Chessboard.create_row4()
        Chessboard.create_row5()
        Chessboard.create_row6()
        Chessboard.create_row7()
        Chessboard.create_row8()

running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('brown')
    
    Chessboard.create_chessboard()