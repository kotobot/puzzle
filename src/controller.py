from model import Board
from view import BoardView, TileView
import pygame
import pickle

from const import GRID_SIZE, TILE_SIZE, FPS, GRAY

class Game:
    def __init__(self, board: Board, screen: pygame.Surface, clock: pygame.time.Clock):
        self.clock = clock
        self.screen = screen
        self.board = board
        self.board_view = BoardView(board)
        self.running = True
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        # Get the tile position from the mouse click
                        x, y = event.pos
                        col = x // TILE_SIZE
                        row = y // TILE_SIZE
                        self.board.move((row, col))
                        self.board.update()
                        self.board_view.draw(self.screen)
                        if self.board.is_solved():
                            print("Puzzle solved!")
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:  # Reset/shuffle with 'r' key
                        self.board.shuffle()
            
            # Draw
            self.screen.fill(GRAY)
            self.board_view.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(FPS)
            
    def save_game(self):
        pickle.dump(self.board, open("save_game.pkl", "wb"))
    
    def load_game(self):
        try:
            self.board = pickle.load(open("save_game.pkl", "rb"))
            self.board.update()
            self.board_view = BoardView(self.board)
        except FileNotFoundError:
            print("No saved game found.")

    def print_board(self):
        print('-' * 15)
        for row in self.board.tiles:
            print(' '.join([str(tile.value) for tile in row]))
            print('\n')
        print('-' * 15)