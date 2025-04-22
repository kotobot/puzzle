from enum import Enum
import pickle
import pygame
import random
import sys

sys.path.append("src")

from const import WIDTH, HEIGHT
from menu import Menu, MenuItem
from model import Board
from controller import Game

# Initialize pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("15 Puzzle")
clock = pygame.time.Clock()

def main():
    board = Board()
    menu = Menu(screen)
    game = Game(board, screen, clock)
    while True:
        selected = menu.run()
        if selected == MenuItem.START:
            board.shuffle()
            game.run()
        elif selected == MenuItem.SAVE:
            game.save_game()
        elif selected == MenuItem.LOAD:
            game.load_game()
            game.run()
        elif selected == MenuItem.EXIT:
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()